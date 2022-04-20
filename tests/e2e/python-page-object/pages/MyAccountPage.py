from pages.BasePage import BasePage
from pages.Locators import MyAccountPageLocators

class MyAccountPage(BasePage):

    def get_username(self):
        return self.get_element(MyAccountPageLocators.FieldUsername).text
