"""Main module."""
import json
# import solscraper.selenium.selenium_driver as selenium_driver


def entrypoint(args):
    # Selenium lines:
    # use_headless_browser = True if 'headless' in args else False
    # floor_prices_dict = selenium_driver.get_floor_prices(use_headless_browser)
    floor_prices_dict = None
    print("Floor prices dict: " + str(json.dumps(floor_prices_dict)))
