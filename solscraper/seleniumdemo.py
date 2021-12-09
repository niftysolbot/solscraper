import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from marketplace.marketplace_base import MarketplaceNames
from marketplace.magiceden import MagicEden
from marketplace.solanart import Solanart

magiceden_markeplace = MagicEden()
solanart_markeplace = Solanart()


def get_driver():
    cur_dir = os.getcwd()
    s = Service(cur_dir + '/binaries/chromedriver')
    options = webdriver.ChromeOptions()
    # TODO comment this for local testing:
    options.add_argument('headless')
    return webdriver.Chrome(service=s, options=options)


driver = get_driver()
for marketplace in [MagicEden(), Solanart()]:
    print("{} [{}] Floor Price: {}".format(MarketplaceNames.SOLLAMAS, marketplace.name,
                                             marketplace.get_floor_price(driver, MarketplaceNames.SOLLAMAS)))
driver.quit()
