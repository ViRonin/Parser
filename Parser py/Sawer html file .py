#  █▀█ ▄▀█ █▀█ █▀ █▀▀ █▀█ 
#  █▀▀ █▀█ █▀▄ ▄█ ██▄ █▀▄ 
     
    
#  █ ░
#  █ ▄
                                  
#  █▄▄ █▄█ █░█ █ █▀█ █▀█ █▄░█ █ █▄░█
#  █▄█ ░█░ ▀▄▀ █ █▀▄ █▄█ █░▀█ █ █░▀█

import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from random import choice
import requests

random2 = [  19, 16, 17, 18]
random1 = [ 16, 17, 18, 20]

# ===================    Parser http   ===================

options = Options()
options.add_experimental_option("prefs", {
"download.download.default_directory"
"download.prompt_for_download": True,
"download.directory_upgrade": True,
"safebrowsing.enabled": False
})

driver = webdriver.Chrome(chrome_options=options,executable_path=r'C:/Users/[YOU_NAME_PC]/Desktop/Projekt/Pythone/env/DATA BOT/chromedriver.exe')
# options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"') # Proxy Если нужно


for i in range (2, 880) :

    url = url = f'https://prom.ua/Televizory;{i}'
    print(url)
    q = requests.get(url)
    result = q.content
    
    driver.get(url)
    sleep(choice(random1))
    
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl', 's')
    sleep(2)
    pyautogui.hotkey('enter')
    # pyautogui.hotkey('enter')
    sleep(choice(random1))
    # Wait for download
    while True:      
        if len(f'https://prom.ua/Televizory;{i}') > 0 and not any('.crdownload' in name for name in (f'https://prom.ua/Televizory;{i}')):
            break
        for name in (f'https://prom.ua/Televizory;{i}'):
            if name.endswith('.crdownload'):
                continue
            if name.endswith('.html'):
                print('Download complete.')
                
                break
            else:
                break  


driver.quit()
sleep(choice(random2)) 

print("================ ВЖУХ  a(＾O ωO＾)a (((((((((●～* ГОТОВО ================")
