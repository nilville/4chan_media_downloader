from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests
import sys

driver = webdriver.Chrome()
if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    print("Usage: python 4chan_media_downloader.py <thread_url>")
    sys.exit(1)

driver.get(url)

if "4chan.org" not in url:
    print("Please provide a valid 4chan thread URL.")
    driver.quit()
    sys.exit(1)
else:
    print(f"Fetching media from: {url}")

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'fileThumb')))
except Exception as e:
    print(f"Error: {e}")
    driver.quit()
    exit()
elem = driver.find_elements(By.CLASS_NAME, 'fileThumb')
for i in elem:
    link = i.get_attribute('href')
    folder_path = '4chan_downloads'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    response = requests.get(link)
    if response.status_code == 200:
        file_name = os.path.join(folder_path, link.split('/')[-1])
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded ---> : {file_name}")
    else:
        print(f"Failed to download [ERROR] : {link}")
time.sleep(2)
driver.quit()
