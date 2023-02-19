from splinter import Browser
from .base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, browser: Browser):
        super(InventoryPage, self).__init__(browser)
        self.locators = {
            "title_text": ('XPATH', '//*[@id="header_container"]/div[2]/span')
        }
        self.page_values = {
            'title_text': 'PRODUCTS'
        }