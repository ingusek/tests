# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from faker import Faker
import unittest
from time import sleep


# DANE TESTOWE
email = "ingus@wp.pl"
login = "Ingusek"
first_name = "Inga"
last_name = "Gajewska"
password = "panda2000"
invalid_password = "ff"


class RegistrationTest(unittest.TestCase):
    """
    Scenariusz : Rejestracja nowego użytkownika w systemie z zajętym adresem email
    """

    def setUp(self):
        # Przygotowanie testu
        # Warunki wstępne testu
        # Otwarcie przeglądarki
        self.driver = webdriver.Chrome()
        # Otwarcie strony
        self.driver.get("http://127.0.0.1/frontend-vue/")
        # Maksymalizacja okna
        self.driver.maximize_window()
        # Ustawienie bezwarunkowego czekania na elementy przy wyszukiwaniu
        # maks. 10 sekund
        self.driver.implicitly_wait(10)
        # Utworzenie obiektu klasy Faker
        self.fake = Faker()
        self.name = self.fake.name()

    def testUserRegister(self):
        login = self.fake.simple_profile()['username']
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Sign up”
        # Szukam elementu
        # self.driver.find_element_by_partial_link_text("Sign up") # Selenium 3
        # Metoda find_element zwraca instancję klasy WebElement
        sign_in_link = driver.find_element(
            By.PARTIAL_LINK_TEXT, "Sign up")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpisz niepoprawny e-mail
        # Znajdź element
        email_input = driver.find_element(By.ID, "input-email")
        # Zastosuj metodę send_keys() żeby wpisać coś w element
        email_input.send_keys(email)
        # 3. Wpsz unikalną nazwę użytkownika”
        login_input = driver.find_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 4. Wpisz hasło
        password_input = driver.find_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 5. Wpisz imię
        firstname_input = driver.find_element(By.ID, "input-first-name")
        firstname_input.send_keys(first_name)
        # 6. Wpisz nazwisko
        lastname_input = driver.find_element(By.ID, "input-last-name")
        lastname_input.send_keys(last_name)
        # 7. Kliknij Register
        register_btn = driver.find_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()
        # Oczekiwany rezultat
        # 8. Sprawdzenie czy pojawił się komunikat o zajętym adresie e-mail
        error_text = driver.find_element(
            By.XPATH, '//div[@class="text-danger message-col col"]').text
        expectedError_text = "Email is already in use."
        self.assertEqual(error_text, expectedError_text)
        sleep(5)

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()  # (verbosity=4)
