from tqdm import tqdm
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui
options = uc.ChromeOptions()
from time import sleep
import random
import os

os.system("taskkill /IM chrome.exe /F") 

options.add_argument("user-data-dir=C:\\Users\sergi\\AppData\\Local\\Google\Chrome\\User Data")
#options.add_argument("user-data-dir=C:\\Users\\1111\\AppData\\Local\\Google\Chrome\\User Data")

driver = uc.Chrome(executable_path=ChromeDriverManager().install(),options=options)
driver.implicitly_wait(6.5)

driver.get("https://web.whatsapp.com")

# wait for whatsapp loading
# sleep(10)

def init(video_path,images_path):
    
    print("Scan Your QR Codes and Press Enter (Press Enter if You're Already Logged In)")
    input()
    
    filenames = ""
    
    if (video_path != ""):
        filenames = read_videos(video_path)
        print(filenames)
    
    elif (images_path != ""):
        filenames = read_images(images_path)
        print(filenames)
    for i__ in tqdm(range(len(filenames))):
        # search_field = driver.find_element(By.XPATH,'//p[contains(@class,"copyable-text selectable-text")]')
        search_field = driver.find_element(By.CLASS_NAME,'selectable-text.copyable-text')
        search_field.click()

        for i in range(15):
            search_field.send_keys(Keys.BACKSPACE)
        
        search_field.send_keys( filenames[i__].split('.')[0] +  Keys.ENTER)
        delay = 1 
        found = False
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'main')))
            found = True
            
            #driver.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
            driver.find_element(By.CSS_SELECTOR,"span[data-icon='attach-menu-plus']").click()
            #driver.find_element(By.CSS_SELECTOR,"button[aria-label='Photos & Videos']").click()
            driver.find_element(By.CSS_SELECTOR,"li[data-testid='mi-attach-media']").click()

            sleep(2)
            p = ""
            if (videos_path != ""):
                p = video_path
            elif (images_path != ""):
                p = images_path
            path__ = p + "\\"+filenames[i__]
            print(path__)
            "D:\whatsapp_images_videos_sender\Images\lifeline.jpg"
            pyautogui.write(path__)
            sleep(2)
            pyautogui.press("enter")
            #myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_33pCO")))
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='send']")))
            myElem.click()
            sleep(2)
        except Exception as e:
            print("main didn't found exception...")
            print(e)
            
def read_videos(path):
    return os.listdir(path)


def read_images(path):
    return os.listdir(path)


def append_output(data):
    with open('output.txt','a') as f:
        f.write(data + "\n")
        
print("1: Images\n2: Videos")
choice = input("Enter number 1 or 2 ")

images_path = ""
videos_path = ""
if (choice == "1"):
    images_path = input("Enter images folder path ")
elif (choice == "2"):
    videos_path = input("Enter videos folder path ")
    
init(videos_path,images_path)

driver.close()

