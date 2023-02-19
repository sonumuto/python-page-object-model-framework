from splinter import Browser
from .base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, browser: Browser):
        super(LoginPage, self).__init__(browser)
        self.locators = {
            'username_text_box': ('ID', 'user-name'),
            'password_text_box': ('ID', 'password'),
            'login_button': ('ID', 'login-button')
        }

    def login(self, username: str, password: str):
        self.type('username_text_box', username)
        self.type('password_text_box', password)
        self.click('login_button')

    def login_wrong_credentials(self):
        self.type('username_text_box', 'invalid_username')
        self.type('password_text_box', 'invalid_password')
