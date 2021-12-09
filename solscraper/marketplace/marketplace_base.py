from enum import Enum


class Marketplace(object):

    def __init__(self, name, base_link):
        self.name = name
        self.base_link = base_link
        self.collections = []

    def get_floor_price(self, driver, collection):
        pass


class MarketplaceNames(str, Enum):
    SOLLAMAS = 'Sollamas',
    DEGEN_APE_ACADEMY = 'Degenerate Ape Academy',
    TURTLES = 'turtles'