import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

cur_dir = os.getcwd()
s=Service(cur_dir + '/binaries/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://www.magiceden.io/marketplace/oorror")
MAGIC_EDEN_FLOOR_PRICE_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/" \
              "div[1]/div[1]/div[1]/span[2]"
e = WebDriverWait(driver, timeout=6).until(lambda d: d.find_elements_by_xpath(MAGIC_EDEN_FLOOR_PRICE_XPATH))
print("Floor price: " + e[0].accessible_name)
print(driver.current_url)
print(driver.title)
driver.quit()
