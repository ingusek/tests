# Import bibliotek
from pickle import TRUE
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
    Scenariusz : Sprawdzanie czy da się wylogować ze strony http://todo.local/frontend-vue/
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

        # 8. Sprawdzenie logowania użytkownika
        sleep(1)
        title = driver.find_element(By.PARTIAL_LINK_TEXT, 'My Account').text
        expectedTitle = "My Account"
        self.assertEqual(title, expectedTitle)

        # 9. Wylogowanie się przez użytkownika-kliknij "Logout"
        logout_btn = driver.find_element(
            By.XPATH, '//a[@href="/frontend-vue/logout"]')
        logout_btn.click()

        # 10. Sprawdzenie wylogowania się przez użytkownika-czy jest klawisz "Login"
        login_btn = driver.find_element(
            By.XPATH, '//a[@href="/frontend-vue/login"]')
        self.assertTrue(login_btn.is_displayed())

        sleep(5)

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()  # (verbosity=4)
