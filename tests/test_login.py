import unittest
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin(BaseTest):

    def test_valid_login(self):
        LoginPage(self.browser).login('standard_user', 'secret_sauce')
        assert InventoryPage(self.browser).is_page_open(), "Page is not open"
