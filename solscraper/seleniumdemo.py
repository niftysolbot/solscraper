import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from marketplace.marketplace import Marketplace

MAGIC_EDEN_FLOOR_PRICE_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/" \
                               "div[1]/div[1]/div[1]/span[2]"

magiceden_markeplace = Marketplace("Magic Eden", "https://www.magiceden.io/marketplace/")


def get_floor_magic_eden(the_driver, collection):
    the_driver.get(magiceden_markeplace.base_link + collection)
    floor_price_element = WebDriverWait(the_driver, timeout=6) \
        .until(lambda d: d.find_elements_by_xpath(MAGIC_EDEN_FLOOR_PRICE_XPATH))
    if floor_price_element and len(floor_price_element) > 0:
        return floor_price_element[0].accessible_name


cur_dir = os.getcwd()
s = Service(cur_dir + '/binaries/chromedriver')
driver = webdriver.Chrome(service=s)
floor_price = get_floor_magic_eden(driver, 'oorror')
print("Floor price of oorror: " + floor_price)
driver.quit()
