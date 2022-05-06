# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from BaseTestCase import BaseTestCase
from faker import Faker
from time import sleep
import unittest
import os

# DANE TESTOWE

class LoginTest(BaseTestCase):

    """
    ID: 005
    Scenariusz : Logowanie się na stronie http://localhost/login przy użyciu poprawnego loginu i poprawnego hasła
    """
    def test_user_login_successfull(self):
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


    """
    ID: 006
    Scenariusz : Logowanie się na stronie http://localhost/login przy użyciu poprawnego loginu i niepoprawnego hasła
    """
    def test_user_login_with_invalid_password(self):
        login = os.environ['LOGIN']
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
        password_input.send_keys("pistacje")
        # 4. Kliknij Login
        register_btn = self.get_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()

        # 8. Sprawdzenie logowania użytkownika
        sleep(1)
        title = self.get_element(
            By.XPATH, '//div[@data-cy="login-error-message"]').text
        expectedTitle = "Your username or password is incorrect. Please try again."
        self.assertEqual(title, expectedTitle)

    """
    ID: 007
    Scenariusz : Logowanie się na stronie http://localhost/login przy użyciu niepoprawnego loginu i poprawnego hasła.
    """
    def test_user_login_with_invalid_username(self):
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
        login_input.send_keys("blednylogin")
        # 3. Wpisz hasło
        password_input = self.get_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 4. Kliknij Login
        register_btn = self.get_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()

        # 8. Sprawdzenie logowania użytkownika
        sleep(1)
        title = self.get_element(
            By.XPATH, '//div[@data-cy="login-error-message"]').text
        expectedTitle = "Your username or password is incorrect."
        self.assertEqual(title, expectedTitle)

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()  # (verbosity=4)
