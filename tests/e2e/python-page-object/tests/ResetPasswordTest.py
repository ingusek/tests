from tests.BaseTest import BaseTest
from tests.TestData import Settings
from time import sleep

class ResetPasswordTest(BaseTest):
    """
    ID: 018
    """
    def test_reset_pasword_successful(self):
        home_page = self.home_page

        login_page = home_page.click_login()

        reset_pasword_page = login_page.click_forgot_password()
        reset_pasword_page.set_email(self.test_data.in_use_email)
        reset_pasword_page.send()

        mail_page = home_page.open_email_box()
        #5. Assercja  "request new email"- assercja potwierdzenia wysłania emaila z linkiem do zmiany hasła

        #6. Sprawdź skrzynkę emailową pod adresem http://127.0.0.1/mailhog/
        #7. Otwórz email "reset hasła"
        #8. Assercja-klawisz resetu hasła
