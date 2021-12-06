import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from marketplace.marketplace import Marketplace

MAGIC_EDEN_FLOOR_PRICE_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/" \
                               "div[1]/div[1]/div[1]/span[2]"

magiceden_markeplace = Marketplace("Magic Eden", "https://www.magiceden.io/marketplace/")
solanart_markeplace = Marketplace("Solanart", "https://solanart.io/collections/")


def get_floor_magic_eden(the_driver, collection):
    the_driver.get(magiceden_markeplace.base_link + collection)
    floor_price_element = WebDriverWait(the_driver, timeout=6) \
        .until(lambda d: d.find_elements_by_xpath(MAGIC_EDEN_FLOOR_PRICE_XPATH))
    if floor_price_element and len(floor_price_element) > 0:
        return floor_price_element[0].accessible_name


def get_floor_solanart(the_driver, collection):
    the_driver.get(solanart_markeplace.base_link + collection)
    beta_accept_button = WebDriverWait(the_driver, timeout=6) \
        .until(lambda d: d.find_elements_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[1]/p[1]/button[1]/span[1]"))
    if len(beta_accept_button) > 0:
        beta_accept_button[0].click()
    the_driver.implicitly_wait(10)
    time.sleep(5)
    # .until(lambda d: d.find_elements_by_class_name("MuiButton-label-451"))
    floor_price_element = WebDriverWait(the_driver, timeout=10) \
        .until(lambda d: d.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/span[1]/div[1]/button[3]/span[1]/div[1]/span[1]"))
    #MuiButton-label-376
    if floor_price_element and len(floor_price_element) > 0:
        print(str(floor_price_element[0].text))


cur_dir = os.getcwd()
s = Service(cur_dir + '/binaries/chromedriver')
options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome(service=s, chrome_options=options)
# floor_price = get_floor_magic_eden(driver, 'oorror')
get_floor_solanart(driver, "sollamas-gen2")
# print("MagicEden Floor price of oorror: " + floor_price)
driver.quit()
