from tests.BaseTest import BaseTest
from time import sleep

class AccountTest(BaseTest):
    """
    My account Tests
    """
    def test_veryfication_user_data_in_page_account(self):
        home_page = self.home_page
        # 1. Click Sign Up
        login_page = home_page.click_login()
 
        # 2. Fill login form
        login_page.fill_in_login_form(
            self.test_data.in_use_login,
            self.test_data.in_use_password,
        )

        # 3. Click Login 
        login_page.login()

        # 4. Goto my account 
        my_account_page = home_page.goto_my_account()
        username = my_account_page.get_username()

        login = self.test_data.in_use_login
        self.assertEqual(username, login.capitalize())
