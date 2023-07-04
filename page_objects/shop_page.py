# put in selectors for call the operations of the test_shop
from seleniumbase import BaseCase


# create class for selectors
class ShopPage(BaseCase):
    search_input = "#woocommerce-product-search-field-0"
    search_btn = "button[value='Search']"
    product_img = ".woocommerce-product-gallery__image"
    no_products_txt = ".woocommerce-info"

    # open the url page for access cmd from test_shop.py
    def open_page(self):
        self.open("https://practice.automationbro.com/shop")
