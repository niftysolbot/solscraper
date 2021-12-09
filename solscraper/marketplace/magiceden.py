from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as SeleniumTimeoutException
from marketplace.marketplace_base import Marketplace, MarketplaceNames
import time


class MagicEden(Marketplace):

    FLOOR_PRICE_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/" \
                        "div[1]/div[1]/div[1]/span[2]"

    NFT_COLLECTION_LOOKUP_DICT = {
        MarketplaceNames.SOLLAMAS: "sollamas",
        MarketplaceNames.DEGEN_APE_ACADEMY: 'degenerate_ape_academy',
        MarketplaceNames.TURTLES: MarketplaceNames.TURTLES
    }

    def __init__(self):
        super().__init__("Magic Eden", "https://www.magiceden.io/marketplace/")

    def get_floor_price(self, driver, collection_key):
        driver.get(self.base_link + self.NFT_COLLECTION_LOOKUP_DICT[collection_key])
        time.sleep(7)
        floor_price_element = None
        try:
            floor_price_element = WebDriverWait(driver, timeout=6) \
                .until(lambda d: d.find_elements_by_xpath(self.FLOOR_PRICE_XPATH))
        except SeleniumTimeoutException:
            pass
        if floor_price_element and len(floor_price_element) > 0:
            return str(floor_price_element[0].accessible_name)
        return None
