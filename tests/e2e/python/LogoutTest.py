# Import bibliotek
from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from BaseTestCase import BaseTestCase
from faker import Faker
from time import sleep
import unittest
import os

# DANE TESTOWE
login = os.environ['LOGIN']
password = os.environ['PASSWORD']

class LogOutTest(BaseTestCase):
   
    """
    Scenariusz : Sprawdzanie czy da się wylogować ze strony http://localhost/
    """
    def test_logout_successfull(self):
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

        # 9. Wylogowanie się przez użytkownika-kliknij "Logout"
        logout_btn = self.get_element(
            By.XPATH, '//a[@href="/logout"]')
        logout_btn.click()

        # 10. Sprawdzenie wylogowania się przez użytkownika-czy jest klawisz "Login"
        login_btn = self.get_element(
            By.XPATH, '//a[@href="/login"]')
        self.assertTrue(login_btn.is_displayed())


if __name__ == '__main__':
    unittest.main()  # (verbosity=4)
