import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from solscraper.marketplace.magiceden import MagicEden
from solscraper.marketplace.solanart import Solanart
from solscraper.marketplace import marketplace_base

magiceden_markeplace = MagicEden()
solanart_markeplace = Solanart()


def _get_driver(use_headless_browser):
    cur_dir = os.getcwd()
    s = Service(cur_dir + '/binaries/chromedriver')
    options = webdriver.ChromeOptions()
    if use_headless_browser:
        options.add_argument('headless')
    return webdriver.Chrome(service=s, options=options)


def get_floor_prices(use_headless_browser):
    driver = _get_driver(use_headless_browser)
    floor_prices_dict = dict()
    for collection in [marketplace_base.MarketplaceNames.SOLLAMAS, marketplace_base.MarketplaceNames.DEGEN_APE_ACADEMY,
                       marketplace_base.MarketplaceNames.TURTLES]:
        marketplace_dict = dict()
        for marketplace in [MagicEden(), Solanart()]:
            marketplace_dict[marketplace.name] = \
                    marketplace.get_floor_price(driver, collection)
            print("{} [{}] Floor Price: {}".format(collection, marketplace.name,
                                                   marketplace.get_floor_price(driver, collection)))
        floor_prices_dict["{}".format(collection)] = marketplace_dict
    driver.quit()
    return floor_prices_dict
