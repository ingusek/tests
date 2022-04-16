from pages.BasePage import BasePage
from pages.Locators import LoginPageLocators

class LoginPage(BasePage):

    def wait_for_login_page(self):
        self.get_element_with_text(LoginPageLocators.PageTitle, 'Login')

    def get_confirm_regitration_text(self):
        return self.get_element(LoginPageLocators.ConfirmRegistrationInfoBox).text
