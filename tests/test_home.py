# import all functionalities for open the driver of chrome bw
from seleniumbase import BaseCase
from page_objects.home_page import HomePAge


class HomeTest(HomePAge):
    # setup method to optimize
    def setUp(self):
        super().setUp()
        print("run before")

        # open home page => set url and run the test
        self.open_page()

    def tearDown(self):
        print("run after")
        super().tearDown()

    def test_home_page(self):
        # assert page title => set title ,and test this
        self.assert_title("Practice E-Commerce Site – Automation Bro")

        # assert logo
        self.assert_element(HomePAge.logo_icon)

        # click on the get started button and assert the url with API
        self.click(HomePAge.get_started_btn)
        get_started_url = self.get_current_url()  # current url match
        self.assert_equal(get_started_url, 'https://practice.automationbro.com/#get-started')
        # partial verification that return the True if is the end of part of url is there
        self.assert_true('get-started' in get_started_url)

        # get the text of the header and assert the value
        self.assert_text("Think different. Make different.", HomePAge.heading_text)

        # scroll to bottom and assert the copyright text
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro", HomePAge.copyright_text)
