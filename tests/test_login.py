import unittest
from tests.base_test import BaseTest
from pages.login_page import LoginPage


class TestLogin(BaseTest):

    def test_valid_login(self):
        LoginPage(self.browser).login('standard_user', 'secret_sauce')
