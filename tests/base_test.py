import unittest
from splinter import Browser
from pages.base_page import BasePage


class BaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = Browser('firefox')
        self.browser.visit("https://www.saucedemo.com")

    def tearDown(self) -> None:
        self.browser.quit()


