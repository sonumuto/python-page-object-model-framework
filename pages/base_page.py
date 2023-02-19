from splinter import Browser


class BasePage:
    """
    Holds shared methods and attributes.

    Attributes
    ----------
    browser: Browser
        Splinter browser object
    url: str
        URL of the web application
    page_values: dict[str, str]
        Element and values that is unique to that page. This dictionary is iterated and elements' values are obtained
        and checked whether values are equal or not.
    locators: dict[str, tuple[str, str]]
        Locators of the elements in the page. Key of the dictionary is the element name. Value of the dictionary is a
        tuple that holds type to find the element by (XPATH, ID, etc.) and locator.
    """

    def __init__(self, browser: Browser, url: str = 'https://www.saucedemo.com/'):
        self.browser = browser
        self.url = url
        self.page_values = {}
        self.locators = {}

    def find_element(self, element_name: str):
        """
        Find the element and return it.

        Parameters
        ----------
        element_name: str
            Element name to be found.

        Returns
        -------
            Web driver element.

        """
        element = self.locators[element_name]
        if element[0] == 'XPATH':
            return self.browser.find_by_xpath(element[1])
        elif element[0] == 'ID':
            return self.browser.find_by_id(element[1])
        elif element[0] == 'NAME':
            return self.browser.find_by_name(element[1])

    def is_page_open(self) -> bool:
        """
        Check if the page is open or not by iterating the page_values dictionary.

        Returns
        -------
        bool
            Return true if the current page is open.

        """
        for key, value in self.page_values.items():
            if self.get_value(key) != value:
                return False
        return True

    def click(self, element_name: str):
        """Find the element by given name and click it."""
        self.find_element(element_name).first.click()

    def type(self, element_name, text: str):
        self.find_element(element_name).type(text)

    def get_value(self, element_name: str) -> str:
        """Get value of the given element."""
        return self.find_element(element_name).value
