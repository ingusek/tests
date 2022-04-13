from pages.BasePage import BasePage
from pages.Locators import HomePageLocators
from pages.RegisterPage import RegisterPage

class HomePage(BasePage):
    """
    Home Page Object
    """
    def click_sign_up(self):
        element = self.get_element(HomePageLocators.SingUpButton)
        element.click()

        # Return next page
        return RegisterPage(self.driver)
