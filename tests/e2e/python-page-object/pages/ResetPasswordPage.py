from pages.BasePage import BasePage
from pages.Locators import ResetPasswordPageLocators

class ResetPasswordPage(BasePage):
    
    def set_email(self,email):
        self.get_element(ResetPasswordPageLocators.InputEmail).send_keys(email)

    def send(self):
        self.get_element(ResetPasswordPageLocators.RequestNewPasswordButton).click()
