from tests.BaseTest import BaseTest
from tests.TestData import Settings
from time import sleep

class TodoTest(BaseTest):

    """
    ID: 010
    Scenariusz : Sprawdzanie funkcjonalności Todo-dostęp do zakładki Todo tylko po zalogowaniu
    """
    def test_access_toto_list_after_login(self):
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

        todo_page = home_page.open_todo_page();


        # 4. Assert
        title = todo_page.get_title()
        expectedTitle = "Todo App"

        self.assertEqual(title, 
            expectedTitle,
        )
