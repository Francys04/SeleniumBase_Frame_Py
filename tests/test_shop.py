from page_objects.shop_page import ShopPage
# import for exceptions from selenium library
from selenium.common.exceptions import NoSuchElementException


class ShopTest(ShopPage):
    def test_search_pds(self):
        # open url page
        self.open_page()

        # search for product
        self.send_keys(self.search_input, "Toys")
        self.click(self.search_btn)

        # assert product image -> verify the image of product
        # if not exist the product img
        try:
            print("Within try block")
            self.assert_element(self.product_img)
        except NoSuchElementException:
            print("Exception Block")
            self.assert_text("No products were found matching your selection.", self.no_products_txt)
