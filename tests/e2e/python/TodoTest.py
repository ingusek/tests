# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from BaseTestCase import BaseTestCase
from faker import Faker
from time import sleep
import unittest
import os

login = os.environ['LOGIN']
password = os.environ['PASSWORD']

class TodoTest(BaseTestCase):
    
    """
    ID: 010
    Scenariusz : Sprawdzanie funkcjonalności Todo-dostęp do zakładki Todo tylko po zalogowaniu
    """
    def test_access_toto_list_after_login(self):
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Login”
        # Szukam elementu
        sign_in_link = self.get_element(
            By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = self.get_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 3. Wpisz hasło
        password_input = self.get_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 4. Kliknij Login
        register_btn = self.get_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"
        Todo_btn = self.get_element(
            By.XPATH, '//a[@href="/todo"]')
        Todo_btn.click()
        sleep(1)

        # 6. Wyświetlenie pola TodoApp
        title = self.get_element(By.TAG_NAME, 'h1').text
        expectedTitle = "Todo App"
        self.assertEqual(title, expectedTitle)

    """
    ID: 011
    Scenariusz : Sprawdzanie funkcjonalności Todo-dodanie nowego wpisu do  listy Todo
    """
    def test_todo_add_new_item(self):
        item = '011_' + self.fake.name()
        # Kroki
        # 1. Kliknij „Login”
        sign_in_link = self.get_element(
            By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = self.get_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 3. Wpisz hasło
        password_input = self.get_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 4. Kliknij Login
        login_btn = self.get_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        login_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"
        Todo_btn = self.get_element(
            By.XPATH, '//a[@href="/todo"]')
        Todo_btn.click()

        name_input = self.get_element(By.ID, "input-name")
        name_input.send_keys(item)

        # 7. Kliknij Add
        Add_btn = self.get_element(
            By.XPATH, '//form//button[@type="submit"]')  # WebElement
        Add_btn.click()
        sleep(1)
        
        # 8. Assercja
        target = self.get_element(
           By.XPATH, '//div[@class="card-deck"]//div[@class="card mb-3"][1]//div[@class="todo-list-group"]/div//span[text()="'+item+'"]')
        self.assertEqual(item, target.text)


    """
    ID: 012
    Scenariusz: Sprawdzanie funkcjonalności Todo-usunięcie pozycji z listy Pending
    """
    def test_todo_delate_item_from_list_pending(self):
        item = '012_' + self.fake.name()
        # Kroki
        # 1. Kliknij „Login”
        sign_in_link = self.get_element(
            By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = self.get_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 3. Wpisz hasło
        password_input = self.get_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 4. Kliknij Login
        register_btn = self.get_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"
        Todo_btn = self.get_element(
            By.XPATH, '//a[@href="/todo"]')
        Todo_btn.click()

        name_input = self.get_element(By.ID, "input-name")
        name_input.send_keys(item)

        # 7. Kliknij Add
        Add_btn = self.get_element(
            By.XPATH, '//form//button[@type="submit"]')  # WebElement
        Add_btn.click()
        sleep(1)

        # 8. Usuń element z listy Pending
        Pending_element = self.get_element(
            By.XPATH, '//div[@class="card-deck"]//div[@class="card mb-3"][1]//div[@class="todo-list-group"]/div//span[text()="'+item+'"]/../../button[1]')  # WebElement
        
        Pending_element.click()
        sleep(1)

        target = self.driver.find_elements(
           By.XPATH, '//div[@class="card-deck"]//div[@class="card mb-3"][1]//div[@class="todo-list-group"]/div//span[text()="'+item+'"]')
        self.assertEqual(len(target), 0)

    """
    ID: 013
    Scenariusz : Przeniesienie wpisu z listy pending do ongoing
    """
    def test_move_item_from_pending_to_ongoing(self):
        item = '013_' + self.fake.name()

        # 1. Strona logowania
        sign_in_link = self.get_element(By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        sign_in_link.click()

        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = self.get_element(By.ID, "input-username")
        login_input.send_keys(login)

        # 3. Wpisz hasło
        password_input = self.get_element(By.ID, "input-password")
        password_input.send_keys(password)

        # 4. Kliknij Login
        login_btn = self.get_element(By.XPATH, '//button[@type="submit"]')  # WebElement
        login_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"
        todo_btn = self.get_element(By.XPATH, '//a[@href="/todo"]')
        todo_btn.click()
        sleep(1)

        name_input = self.get_element(By.ID, "input-name")
        name_input.send_keys(item)

        # 7. Kliknij Add
        Add_btn = self.get_element(By.XPATH, '//form//button[@type="submit"]')  # WebElement
        Add_btn.click()
        sleep(1)

        Next_btn = self.get_clickable_element(By.XPATH, 
            '//div[@class="card-deck"]//div[@class="card mb-3"][1]//div[@class="todo-list-group"]/div//span[text()="'+item+'"]/../../button[2]'
        )
        Next_btn.click()
        sleep(1)

        # 8. Assercja
        target = self.get_element(
           By.XPATH, '//div[@class="card-deck"]//div[@class="card mb-3"][2]//div[@class="todo-list-group"]/div//span[text()="'+item+'"]')
        self.assertEqual(item, target.text)

    """
    ID: 014
    Scenariusz : Przeniesienie wpisu z listy ongoing do completed
    """
    def test_move_item_from_pending_to_ongoing(self):
        item = '014_' + self.fake.name()

        # 1. Strona logowania
        sign_in_link = self.get_element(By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        sign_in_link.click()

        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = self.get_element(By.ID, "input-username")
        login_input.send_keys(login)

        # 3. Wpisz hasło
        password_input = self.get_element(By.ID, "input-password")
        password_input.send_keys(password)

        # 4. Kliknij Login
        login_btn = self.get_element(By.XPATH, '//button[@type="submit"]')  # WebElement
        login_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"
        todo_btn = self.get_element(By.XPATH, '//a[@href="/todo"]')
        todo_btn.click()
        sleep(1)

        name_input = self.get_element(By.ID, "input-name")
        name_input.send_keys(item)
        
        # 7. Kliknij Add
        Add_btn = self.get_element(By.XPATH, '//form//button[@type="submit"]')  # WebElement
        Add_btn.click()
        sleep(1)

        Next_btn = self.get_clickable_element(By.XPATH, 
            '//div[@class="card-deck"]//div[@class="card mb-3"][1]//div[@class="todo-list-group"]/div//span[text()="'+item+'"]/../../button[2]')
        Next_btn.click()
        sleep(1)
        
        Next_Completed_btn = self.get_clickable_element(By.XPATH, 
            '//div[@class="card-deck"]//div[@class="card mb-3"][2]//div[@class="todo-list-group"]/div//span[text()="'+item+'"]/../../button[3]')
        Next_Completed_btn.click()
        sleep(1)
        
        # 8. Assercja
        target = self.get_element(
           By.XPATH, '//div[@class="card-deck"]//div[@class="card mb-3"][3]//div[@class="todo-list-group"]/div//span[text()="'+item+'"]')
        self.assertEqual(item, target.text)

    """
    ID: 016
    Scenariusz : Umieszczenie na liście pending pozycji o tej samej nazwie
    """
    def test_add_item_to_pending_with_name_already_in_use(self):
        item = '016_'  + self.fake.name();
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Login”
        sign_in_link = self.get_element(
            By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = self.get_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 3. Wpisz hasło
        password_input = self.get_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 4. Kliknij Login
        register_btn = self.get_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"
        Todo_btn = self.get_element(
            By.XPATH, '//a[@href="/todo"]')
        Todo_btn.click()
        sleep(1)

        # 6. Wyświetlenie pola TodoApp
        title = self.get_element(By.TAG_NAME, 'h1').text
        expectedTitle = "Todo App"
        self.assertEqual(title, expectedTitle)

        name_input = self.get_element(By.ID, "input-name")
        name_input.send_keys(item)

        # 7. Kliknij Add
        Add_btn = self.get_element(
            By.XPATH, '//form//button[@type="submit"]')  # WebElement
        Add_btn.click()
        Add_btn.click()
        sleep(1)

        # 8. Assercja
        target = self.driver.find_elements(
           By.XPATH, '//div[@class="card-deck"]//div[@class="card mb-3"][1]//div[@class="todo-list-group"]/div//span[text()="'+item+'"]')
        self.assertEqual(len(target), 2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()  # (verbosity=4)
