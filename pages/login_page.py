from splinter import Browser
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = {
        'username_text_box': ('ID', 'user-name'),
        'password_text_box': ('ID', 'password'),
        'login_button': ('ID', 'login-button')
    }

    def __init__(self, browser: Browser):
        super(LoginPage, self).__init__(browser)

    def login(self, username: str, password: str):
        self.type(self.locators["username_text_box"], username)
        self.type(self.locators["password_text_box"], password)
        self.click(self.locators["login_button"])
