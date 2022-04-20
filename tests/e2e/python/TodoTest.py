# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from faker import Faker
from time import sleep
import unittest
import os

class TodoTest(unittest.TestCase):
    

    def setUp(self):
        # Przygotowanie testu
        # Warunki wstępne testu
        # Otwarcie przeglądarki
        self.driver = webdriver.Chrome()
        # Otwarcie strony
        self.driver.get(os.environ['APP_URL'])
        # Maksymalizacja okna
        self.driver.maximize_window()
        # Ustawienie bezwarunkowego czekania na elementy przy wyszukiwaniu
        # maks. 10 sekund
        self.driver.implicitly_wait(10)

    """
    Scenariusz : Sprawdzanie funkcjonalności Todo-dostęp do zakładki Todo tylko po zalogowaniu
    """
    def test_access_toto_list_after_login(self):
        login = os.environ['LOGIN']
        password = os.environ['PASSWORD']
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Login”
        # Szukam elementu
        # self.driver.find_element_by_partial_link_text("Login") # Selenium 3
        # Metoda find_element zwraca instancję klasy WebElement
        sign_in_link = driver.find_element(
            By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = driver.find_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 3. Wpisz hasło
        password_input = driver.find_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 4. Kliknij Login
        register_btn = driver.find_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"
        Todo_btn = driver.find_element(
            By.XPATH, '//a[@href="/frontend-vue/todo"]')
        Todo_btn.click()

        # 6. Wyświetlenie pola TodoApp
        sleep(5)
        title = driver.find_element(By.TAG_NAME, 'h1').text
        expectedTitle = "Todo App"
        self.assertEqual(title, expectedTitle)
        sleep(5)

    """
    Scenariusz : Sprawdzanie funkcjonalności Todo-dodanie nowego wpisu do  listy Todo
    """
    def test_todo_add_new_item(self):
        login = os.environ['LOGIN']
        password = os.environ['PASSWORD']
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Login”
        # Szukam elementu
        # self.driver.find_element_by_partial_link_text("Login") # Selenium 3
        # Metoda find_element zwraca instancję klasy WebElement
        sign_in_link = driver.find_element(
            By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = driver.find_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 3. Wpisz hasło
        password_input = driver.find_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 4. Kliknij Login
        login_btn = driver.find_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        login_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"
        Todo_btn = driver.find_element(
            By.XPATH, '//a[@href="/frontend-vue/todo"]')
        Todo_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"        
        # 8. Kliknij Add (dodanie do Ongoing)
        name_input = driver.find_element(By.ID, "input-name")
        name_input.send_keys("śniadanie")

        # 7. Kliknij Add
        Add_btn = driver.find_element(
            By.XPATH, '//form//button[@type="submit"]')  # WebElement
        Add_btn.click()
        sleep(1)

        """Scenariusz: Sprawdzanie funkcjonalności Todo-usunięcie pozycji z listy Pending
        """

    def test_todo_delate_item_from_list_pending(self):
        login = os.environ['LOGIN']
        password = os.environ['PASSWORD']
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Login”
        # Szukam elementu
        # self.driver.find_element_by_partial_link_text("Login") # Selenium 3
        # Metoda find_element zwraca instancję klasy WebElement
        sign_in_link = driver.find_element(
            By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = driver.find_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 3. Wpisz hasło
        password_input = driver.find_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 4. Kliknij Login
        register_btn = driver.find_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"
        Todo_btn = driver.find_element(
            By.XPATH, '//a[@href="/frontend-vue/todo"]')
        Todo_btn.click()

        # 6. Wyświetlenie pola TodoApp
        sleep(5)
        title = driver.find_element(By.TAG_NAME, 'h1').text
        expectedTitle = "Todo App"
        self.assertEqual(title, expectedTitle)

        name_input = driver.find_element(By.ID, "input-name")
        name_input.send_keys("śniadanie")

        # 7. Kliknij Add
        Add_btn = driver.find_element(
            By.XPATH, '//form//button[@type="submit"]')  # WebElement
        Add_btn.click()

       # 8. Usuń element z listy Pending
        Pending_element = driver.find_element(
            By.XPATH, '//div[@class="card-body"]//button[@type="button"][1]')  # WebElement
        Pending_element.click()

        sleep(5)

    """
    Scenariusz : Umieszczenie na liście Pending pozycji o tej samej nazwie
    """
    def test_add_item_to_pending_with_name_already_in_use(self):
        login = os.environ['LOGIN']
        password = os.environ['PASSWORD']
        faker = Faker()
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Login”
        # Szukam elementu
        # self.driver.find_element_by_partial_link_text("Login") # Selenium 3
        # Metoda find_element zwraca instancję klasy WebElement
        sign_in_link = driver.find_element(
            By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = driver.find_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 3. Wpisz hasło
        password_input = driver.find_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 4. Kliknij Login
        register_btn = driver.find_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"
        Todo_btn = driver.find_element(
            By.XPATH, '//a[@href="/frontend-vue/todo"]')
        Todo_btn.click()

        # 6. Wyświetlenie pola TodoApp
        sleep(5)
        title = driver.find_element(By.TAG_NAME, 'h1').text
        expectedTitle = "Todo App"
        self.assertEqual(title, expectedTitle)

        name_input = driver.find_element(By.ID, "input-name")
        name_input.send_keys(faker.name())

        # 7. Kliknij Add
        Add_btn = driver.find_element(
            By.XPATH, '//form//button[@type="submit"]')  # WebElement
        Add_btn.click()
        Add_btn.click()

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()  # (verbosity=4)