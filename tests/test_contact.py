from seleniumbase import BaseCase


class ContactTest(BaseCase):
    def test_contact_page(self):
        # open url
        self.open("https://sdetunicorns.com/contact/")

        # fill in all the fields
        self.send_keys('contact-name input', 'alex')
        self.send_keys('contact-email input', 'alexmorohai1997@gmail.com')
        self.send_keys('contact-phone input', '12356547')
        self.send_keys('contact-message textarea', 'This is my message of this test')

        # click the submit bottom
        self.click("recaptcha-checkbox-border")
        self.click("elementor-field-group elementor-column elementor-field-type-submit elementor-col-100 "
                   "e-form__buttons")

        # verify submit message
        self.assert_text("Your submission was successful.", "div[role=alert]")