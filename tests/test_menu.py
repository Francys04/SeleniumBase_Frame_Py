from tests.test_home import HomeTest
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
