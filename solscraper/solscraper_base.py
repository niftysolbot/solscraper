"""Main module."""
import solscraper.selenium_driver as selenium_driver
import json


def entrypoint(args):
    use_headless_browser = True if 'headless' in args else False
    floor_prices_dict = selenium_driver.get_floor_prices(use_headless_browser)
    print("Floor prices dict: " + str(json.dumps(floor_prices_dict)))
