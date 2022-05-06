from tests.BaseTest import BaseTest
from tests.TestData import Settings
from time import sleep

class LoginTest(BaseTest):

    """
    ID: 005
    """
    def test_login_success(self):
        home_page = self.home_page
        # 1. Click Login
        login_page = home_page.click_login()
 
        # 2. Fill login form
        login_page.fill_in_login_form(
            self.test_data.in_use_login,
            self.test_data.in_use_password,
        )

        # 3. Click Login 
        login_page.login()
        button = home_page.get_my_account_button()

        # 4. Asserts
        title = button.text
        expectedTitle = "My Account"
        self.assertEqual(title, expectedTitle)

    """
    ID: 006
    """
    def test_user_login_with_invalid_password(self):
        home_page = self.home_page
        # 1. Click Sign Up
        login_page = home_page.click_login()
 
        # 2. Fill login form
        login_page.fill_in_login_form(
            self.test_data.in_use_login,
            self.test_data.invalid.password,
        )
        # 3. Click Login 
        login_page.login()
        Error_message = login_page.get_error_message()

        # 4.Asserts
        expectedError_message = "Your username or password is incorrect. Please try again."
        self.assertEqual(Error_message, expectedError_message)


    """
    ID: 007
    """
    def test_user_login_with_invalid_username(self):
        home_page = self.home_page
        # 1. Click Sign Up
        login_page = home_page.click_login()
 
        # 2. Fill login form
        login_page.fill_in_login_form(
            self.test_data.invalid.login,
            self.test_data.in_use_password,
        )
        # 3. Click Login 
        login_page.login()
        Error_message = login_page.get_error_message()

        # 4.Asserts
        expectedError_message = "Your username or password is incorrect."
        self.assertEqual(Error_message, expectedError_message)

        
        