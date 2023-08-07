""" The seleniumbase library is a Python library that provides a simplified way to write and run 
Selenium automation tests using popular testing frameworks like unittest and pytest. 
The BaseCase class is a foundational class provided by seleniumbase that you can use to create your test cases."""
from seleniumbase import BaseCase


"""# call the selectors which will access with url access"""
class CartPage(BaseCase):
    converse_add_to_cart_btn = "a[aria-label='Add “Branded Converse” to your cart']"
    cart_count_text = "li[class='menu-item tg-menu-item tg-menu-item-cart '] span[class='count']"
    subtotal_text = "td[class='product-subtotal']"
    product_quantity_input = "input[id^='quantity']"
    update_cart_btn = "button[name='update_cart']"
    loading_overlay = ".woocommerce-cart-form div[class*='blockOverlay']"

    # open url
    def open_page(self):
        self.open("https://practice.automationbro.com/cart")
