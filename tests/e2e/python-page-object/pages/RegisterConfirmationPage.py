from pages.BasePage import BasePage
from pages.Locators import RegisterConfirmationPageLocators
from pages.Locators import RegisterPageLocators

class RegisterConfirmationPage(BasePage):
    """
    Register confirmation page
    """
    def get_info_box(self):
        """
        Info Box
        """
        return self.get_element(RegisterConfirmationPageLocators.WelcomeAfterRegisterText)

    def wait_for_regitration_success(self):
        self.get_element_with_text(RegisterPageLocators.Title, 'You are successfully registered.').text
