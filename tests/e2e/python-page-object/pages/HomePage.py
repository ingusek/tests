from pages.BasePage import BasePage
from pages.Locators import HomePageLocators
from pages.RegisterPage import RegisterPage
from pages.MailHogPage import MailHogPage

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
    Goto Email Box
    """
    def open_email_box(self, url):
        self.driver.get(url)
        return MailHogPage(self.driver)
