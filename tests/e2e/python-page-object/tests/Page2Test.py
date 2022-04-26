from tests.BaseTest import BaseTest
from tests.TestData import Settings
from time import sleep

class Page2Test(BaseTest):
    """
    Page2 Test
    """
    def test_display_page2(self):
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

        # 4.Sprawdzenie logowania użytkownika
        title = button.text
        expectedTitle = "My Account"
        self.assertEqual(title, expectedTitle)


        #5. Kliknięcie w menu Simple Page i wybór pozycji Page2
        page2 = home_page.open_page2()

        #6. Sprawdzenie tytułu strony
        title = page2.get_title()
        self.assertEqual(title, "Sample page 2")
        