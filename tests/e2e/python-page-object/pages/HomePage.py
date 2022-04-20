from pages.BasePage import BasePage
from pages.Locators import HomePageLocators
from pages.RegisterPage import RegisterPage
from pages.MailHogPage import MailHogPage
from pages.MyAccountPage import MyAccountPage
from pages.LoginPage import LoginPage

class HomePage(BasePage):
    """
    Home Page Object
    """
    def click_sign_up(self):
        element = self.get_element(HomePageLocators.SingUpButton)
        element.click()

        # Return next page
        return RegisterPage(self.driver)

    """
    Go to Email Box
    """
    def open_email_box(self, url):
        self.driver.get(url)
        return MailHogPage(self.driver)

    def click_login(self):
        element = self.get_element(HomePageLocators.LoginButton)
        element.click()

        return LoginPage(self.driver)

    def get_my_account_button(self):
        element = self.get_element(HomePageLocators.MyAccountButton)
        return element


    """
    LogOut
    """ 
    def click_logout(self):
        element = self.get_element(HomePageLocators.LogoutButton)
        element.click()

    """
    Get login button
    """
    def get_login_button(self):
        element = self.get_element(HomePageLocators.LoginButton)
        return element

    """
    Goto my account
    """
    def goto_my_account(self):
        self.get_element(HomePageLocators.MyAccountButton).click()
        return MyAccountPage(self.driver)

