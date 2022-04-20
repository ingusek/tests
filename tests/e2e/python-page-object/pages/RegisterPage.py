from time import sleep
from pages.BasePage import BasePage
from pages.RegisterConfirmationPage import RegisterConfirmationPage
from pages.Locators import RegisterPageLocators

class RegisterPage(BasePage):
    """
    Fill in the form
    """
    def fill_in_registration_form(self, email, first_name, last_name, password, login):
        self.get_element(RegisterPageLocators.RegisterEmailInput).send_keys(email)   
        self.get_element(RegisterPageLocators.RegisterFirstNameInput).send_keys(first_name)   
        self.get_element(RegisterPageLocators.RegisterLastNameInput).send_keys(last_name)        
        self.get_element(RegisterPageLocators.RegisterPasswordInput).send_keys(password)   
        self.get_element(RegisterPageLocators.RegisterUsernameInput).send_keys(login)   

    def get_danger_message(self):
        return self.get_element(RegisterPageLocators.RegisterDangerMessage).text

    def register(self):
        self.get_element(RegisterPageLocators.RegisterButton).click()
        return RegisterConfirmationPage(self.driver)

    def is_button_enabled(self):
        return self.get_element(RegisterPageLocators.RegisterButton).is_enabled()
