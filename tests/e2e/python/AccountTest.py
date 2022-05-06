# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from BaseTestCase import BaseTestCase
from faker import Faker
import unittest
from time import sleep
import os

class AccountTest(BaseTestCase):

    """
    ID: 008
    Scenariusz : Sprawdzanie danych użytkownika na stronie http://localhost/ po zalogowaniu się
    """
    def test_veryfication_user_data_in_page_account(self):
        login = os.environ['LOGIN']
        password = os.environ['PASSWORD']
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

        # 8. Sprawdzenie logowania użytkownika
        sleep(1)
        title = self.get_element(By.PARTIAL_LINK_TEXT, 'My Account').text
        expectedTitle = "My Account"
        self.assertEqual(title, expectedTitle)

        # 9. Kliknięcie w "My Account"
        self.get_element(By.PARTIAL_LINK_TEXT, 'My Account').click()
        sleep(1)
        username = self.get_element(
            By.XPATH, "//div[@class='card-body']//div/fieldset/div").text
        self.assertEqual(username, login)

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()  # (verbosity=4)