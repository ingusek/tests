from pages.BasePage import BasePage
from pages.Locators import MailHogPageLocators
from pages.LoginPage import LoginPage

class MailHogPage(BasePage):

    def confirm_registration(self):
        email_link = self.get_element(MailHogPageLocators.EmailFirstRow)  # WebElement
        email_link.click()

        self.switch_to_frame(MailHogPageLocators.PreviewIframe)
        confirm_email_url = self.get_element(MailHogPageLocators.EmailRegistrationConfirmButton)
        confirm_email_url.click()
        self.switch_to_window()

        return LoginPage(self.driver)
