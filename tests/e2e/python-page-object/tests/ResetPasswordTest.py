from tests.BaseTest import BaseTest
from tests.TestData import Settings
from time import sleep

class ResetPasswordTest(BaseTest):
    """
    ID: 018
    """
    def test_reset_pasword_successful(self):
        home_page = self.home_page
        # 1. Click Login
        login_page = home_page.click_login()

        #2. Kliknij w opcje ”przypomnij hasło”
        reset_pasword_page = login_page.click_forgot_password()

        #3. Wpisz adres email w polu „znajdź hasło”
        reset_pasword_page.set_email(self.test_data.in_use_email)
        #4. Kliknij „żadanie nowego hasła”
        reset_pasword_page.send()
        #5. Assercja  "request new email"- assercja potwierdzenia wysłania emaila z linkiem do zmiany hasła

        #6. Sprawdź skrzynkę emailową pod adresem http://127.0.0.1/mailhog/
        #7. Otwórz email "reset hasła"
        #8. Assercja-klawisz resetu hasła