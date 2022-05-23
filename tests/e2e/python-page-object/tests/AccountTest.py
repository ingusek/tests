from tests.BaseTest import BaseTest
from time import sleep

class AccountTest(BaseTest):
    """
    ID: 008
    """
    def test_veryfication_user_data_in_page_account(self):
        home_page = self.home_page

        login_page = home_page.click_login()
        login_page.fill_in_login_form(
            self.test_data.in_use_login,
            self.test_data.in_use_password,
        )
        login_page.login()
        
        my_account_page = home_page.goto_my_account()
        username = my_account_page.get_username()

        login = self.test_data.in_use_login
        self.assertEqual(username, login.capitalize())
