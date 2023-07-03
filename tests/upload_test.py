from seleniumbase import BaseCase
import os


class UploadTest(BaseCase):
    def test_visible_upload(self):
        # open url
        self.open("https://practice.automationbro.com/cart/")

        # get file path
        file_path = './data/logo.jpg'

        # add js code
        remove_hidden_class = "document.getElementById('upload_1).classLsit.remove('file_input_hidden')"
        self.add_js_code(remove_hidden_class)

        # upload file
        self.choose_file("#input_1", file_path)

        # click the upload bottom
        self.click("#upload_1")

        # assert file uploaded text
        self.assert_text("File logo.jpg uploaded successfully", "label")


