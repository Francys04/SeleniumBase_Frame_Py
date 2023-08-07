"""This line imports the HomeTest class from the test_home module located in the tests package. 
This suggests that there is a test suite or set of test cases related to the home page, 
and the HomeTest class likely contains the test methods for those cases."""
from tests.test_home import HomeTest
"""This line imports the HomePAge class from the home_page module located in the page_objects package. 
This suggests that there is a Page Object model being used in the test automation project, 
and the HomePAge class likely represents the Page Object for the home page of the application being tested."""
from page_objects.home_page import HomePAge
# from seleniumbase import BaseCase


class MenuTest(HomeTest):
    # test the menu bar of https://sdetunicorns.com/
    def test_menu_links(self):
        expected_links = ['HOME', 'COURSES', 'BLOG', 'COMMUNITY', 'CONTACT', 'LOGIN', 'JOIN ACADEMY']

        # open url
        self.open("https://sdetunicorns.com/")

        # find the elements of links
        menu_links_el = self.find_elements(HomePAge.menu_links)

        # loop through our menu links
        for idx, link_el in enumerate(menu_links_el):
            print(idx, link_el.text)
            self.assertEqual(expected_links[idx], link_el.text)
