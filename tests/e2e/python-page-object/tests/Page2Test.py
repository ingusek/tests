from tests.BaseTest import BaseTest

class Page2Test(BaseTest):
    """
    ID: 017
    """
    def test_display_page2(self):
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

        page2 = home_page.open_page2()
        self.assertEqual(page2.get_title(), "Sample page 2")
