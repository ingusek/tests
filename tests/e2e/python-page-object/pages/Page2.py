from pages.BasePage import BasePage
from pages.Locators import Page2Locators

class Page2(BasePage):

    def get_title(self):
        return self.get_element(Page2Locators.Page2Title).text
        