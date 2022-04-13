from pages.BasePage import BasePage
from pages.Locators import RegisterConfirmationPageLocators

class RegisterConfirmationPage(BasePage):
    """
    Register confirmation page
    """
    def get_info_box(self):
        """
        Info Box
        """
        return self.get_element(RegisterConfirmationPageLocators.WelcomeAfterRegisterText)
