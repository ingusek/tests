from tests.BaseTest import BaseTest

class LogOutTest(BaseTest):
    """
    ID: 009
    """
    def test_logout_success(self):
        home_page = self.home_page

        login_page = home_page.click_login()
        login_page.fill_in_login_form(
            self.test_data.in_use_login,
            self.test_data.in_use_password,
        )
        login_page.login()

        button = home_page.get_my_account_button()

        expectedTitle = "My Account"
        self.assertEqual(button.text, expectedTitle)

        home_page.click_logout()
        login_button = home_page.get_login_button()
        self.assertTrue(login_button.is_displayed())
