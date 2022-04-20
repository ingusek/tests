from pages.BasePage import BasePage
from pages.Locators import LoginPageLocators

class LoginPage(BasePage):

    def wait_for_login_page(self):
        self.get_element_with_text(LoginPageLocators.PageTitle, 'Login')

    def get_confirm_regitration_text(self):
        return self.get_element(LoginPageLocators.ConfirmRegistrationInfoBox).text

    def fill_in_login_form(self, login, password):
        self.get_element(LoginPageLocators.FieldLogin).send_keys(login)
        self.get_element(LoginPageLocators.FieldPassword).send_keys(password)

    def login(self):
        self.get_element(LoginPageLocators.ButtonLogin).click()

    def get_error_message(self):
        return self.get_element(LoginPageLocators.ErrorLoginMessage).text
        

