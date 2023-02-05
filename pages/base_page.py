from splinter import Browser
import logging


class BasePage:
    def __init__(self, browser: Browser, url: str='https://www.saucedemo.com/'):
        self.browser = browser
        self.url = url

    def find_element(self, element: list[str]):
        if element[0] == 'XPATH':
            return self.browser.find_by_xpath(element[1])
        elif element[0] == 'ID':
            return self.browser.find_by_id(element[1])
        elif element[0] == 'NAME':
            return self.browser.find_by_name(element[1])

    def click(self, element: list[str]):
        self.find_element(element).first.click()

    def type(self, element: list[str], text: str):
        self.find_element(element).type(text)
