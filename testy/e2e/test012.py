# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from faker import Faker
from time import sleep
import unittest
import os

# DANE TESTOWE
login = os.environ['LOGIN']
password = os.environ['PASSWORD']

class RegistrationTest(unittest.TestCase):
    """
    Scenariusz : Sprawdzanie funkcjonalności Todo-dodanie nowego wpisu do  listy Todo
    """

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

    def testUserRegister(self):
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
        # 5. Kliknięcie w zakładkę "Todo"        # 8. Kliknij Add (dodanie do Ongoing)
        Add_btn = driver.find_element(
            By.XPATH, '//form//button[@type="submit"]')  # WebElement
        Add_btn.click()
        Add_btn = driver.find_element(
            By.XPATH, '//div[@class="todo-list-group"]//div[@data-name="todo-pending-list-0"]')  # WebElement
        Add_btn.click()

        # 9. Przeniesienie pozycji z listy Pending  do listy Ongoing
       # Przenies_element = driver.find_element(
        # By.XPATH, '//div[@class="l-2 todo-ongoing-span"][1]')  # WebElement
       # Przenies_element.send_keys("śniadanie")
        sleep(1)
        source = driver.find_element(
            By.XPATH, '//div[@data-name="todo-pending-list-0"]')
        target = driver.find_element(
            By.XPATH, '//div[@class="card-deck"]//div[@class="card mb-3"][2]//div[@class="todo-list-group"]')
        actions2 = ActionChains(driver)
        actions2.drag_and_drop_by_offset(
            source, 650, 140).pause(2).release(target).perform()
        # actions2.click_and_hold(source).move_to_element(target).pause(5).release(target).perform()
        # drag_and_drop(driver, source, target)

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

        sleep(5)

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()  # (verbosity=4)
