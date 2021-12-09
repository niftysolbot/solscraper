from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as SeleniumTimeoutException
from marketplace.marketplace_base import Marketplace, MarketplaceNames
import time


class Solanart(Marketplace):

    FLOOR_PRICE_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/" \
                        "span[1]/div[1]/button[3]/span[1]/div[1]/span[1]"

    NFT_COLLECTION_LOOKUP_DICT = {
        MarketplaceNames.SOLLAMAS: "sollamas-gen2"
    }

    def __init__(self):
        super().__init__("Solanart", "https://solanart.io/collections/")

    def get_floor_price(self, driver, collection_key):
        driver.get(self.base_link + self.NFT_COLLECTION_LOOKUP_DICT[collection_key])
        driver.implicitly_wait(6)
        beta_accept_button = None
        try:
            beta_accept_button = WebDriverWait(driver, timeout=6) \
                .until(
                lambda d: d.find_elements_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[1]/p[1]/button[1]/span[1]"))
        except SeleniumTimeoutException:
            pass
        if beta_accept_button and len(beta_accept_button) > 0:
            beta_accept_button[0].click()
        driver.implicitly_wait(10)
        time.sleep(7)
        floor_price = self.__get_floor_price(driver)
        while not floor_price or floor_price.strip() == '0':
            time.sleep(2)
            floor_price = self.__get_floor_price(driver)
        return floor_price

    def __get_floor_price(self, driver):
        try:
            floor_price_element = WebDriverWait(driver, timeout=6) \
                .until(lambda d: d.find_elements_by_xpath(self.FLOOR_PRICE_XPATH))
            if floor_price_element and len(floor_price_element) > 0:
                # print("Floor price: " + str(floor_price_element[0].text))
                return str(floor_price_element[0].text)
        except SeleniumTimeoutException:
            self.__get_floor_price(driver)
        return None

