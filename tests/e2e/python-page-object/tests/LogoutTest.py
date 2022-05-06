from tests.BaseTest import BaseTest

class LogOutTest(BaseTest):
    """
    ID: 009
    """
    def test_logout_success(self):
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
        button = home_page.get_my_account_button()

        # 4. Login Assert
        title = button.text
        expectedTitle = "My Account"
        self.assertEqual(title, expectedTitle)

        # 5. Click "Logout"
        home_page.click_logout()

        # 6. Asserts
        login_button = home_page.get_login_button()
        self.assertTrue(login_button.is_displayed())
