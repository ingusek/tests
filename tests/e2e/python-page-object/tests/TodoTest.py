from tests.BaseTest import BaseTest
from time import sleep

class TodoTest(BaseTest):

    """
    Base class for each test
    """
    def setUp(self):
        BaseTest.setUp(self);
        login_page = self.home_page.click_login()
        login_page.fill_in_login_form(
            self.test_data.in_use_login,
            self.test_data.in_use_password,
        )
        login_page.login()

    """
    ID: 010
    Scenariusz : Sprawdzanie funkcjonalności Todo-dostęp do zakładki Todo tylko po zalogowaniu
    """
    def test_access_toto_list_after_login(self):
        todo_page = self.home_page.open_todo_page();
        title = todo_page.get_title()

        expectedTitle = "Todo App"
        self.assertEqual(title, 
            expectedTitle,
        )

    """
    ID: 011
    Scenariusz : Sprawdzanie funkcjonalności Todo-dodanie nowego wpisu do  listy Todo
    """
    def test_todo_add_new_item(self):
        item = self.test_data.get_item_name('011')
        todo_page = self.home_page.open_todo_page();
        todo_page.add_item(item)
        
        element = todo_page.get_item_from_pending_list_by_name(item)
        self.assertEqual(item, element.text)


    """
    ID: 012
    Scenariusz: Sprawdzanie funkcjonalności Todo-usunięcie pozycji z listy Pending
    """
    def test_todo_delate_item_from_list_pending(self):
        item = self.test_data.get_item_name('012')

        todo_page = self.home_page.open_todo_page();
        todo_page.add_item(item)

        todo_page.remove_item_from_pending_list_by_name(item)

        sleep(1)
        elements = todo_page.get_items_from_pending_list_by_name(item)
        self.assertEqual(len(elements), 0)

    """
    ID: 013
    Scenariusz : Przeniesienie wpisu z listy pending do ongoing
    """
    def test_move_item_from_pending_to_ongoing(self):
        item = self.test_data.get_item_name('013')

        todo_page = self.home_page.open_todo_page();
        todo_page.add_item(item)

        todo_page.move_from_pending_to_ongiong(item)
        element = todo_page.get_item_from_ongiong_list_by_name(item)
        self.assertEqual(item, element.text)

    """
    ID: 014
    Scenariusz : Przeniesienie wpisu z listy ongoing do completed
    """
    def test_move_item_from_ongoing_to_completed(self):
        item = self.test_data.get_item_name('014')

        todo_page = self.home_page.open_todo_page();
        todo_page.add_item(item)

        todo_page.move_from_pending_to_ongiong(item)
        todo_page.move_from_ongiong_to_completed(item)

        element = todo_page.get_item_from_completed_list_by_name(item)
        self.assertEqual(item, element.text)

    """
    ID: 015
    Scenariusz : Umieszczenie na liście pending pozycji o tej samej nazwie
    """
    def test_add_item_to_pending_with_name_already_in_use(self):
        item = self.test_data.get_item_name('016')
       
        todo_page = self.home_page.open_todo_page();
        todo_page.add_item(item)
        todo_page.add_item(item)
        
        sleep(1)
        elements = todo_page.get_items_from_pending_list_by_name(item)
        self.assertEqual(len(elements), 2)
