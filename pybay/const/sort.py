from enum import Enum

class Sort(Enum):
    price_asc = "price"
    price_desc = "-price"
    distance = "distance"
    listing_date = "newlyListed"
