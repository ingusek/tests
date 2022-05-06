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
login = os.environ['LOGIN']
password = os.environ['PASSWORD']
expectedTitle= "Sample page 2"

class Page2Test(BaseTestCase):

    """
    ID: 017
    Scenariusz : Wyświetlenie informacji z podstrony Page2
    """
    def test_display_page2(self):
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
        self.assertEqual(title, "My Account")

        #9. Kliknięcie w menu Simple Page
        SimplePage_menu = self.get_element(
            By.PARTIAL_LINK_TEXT, 'Sample Page')  # WebElement
        SimplePage_menu.click()
        sleep(1)

        #10. Wybór pozycji Page2
        Page2_menu = self.get_element(
            By.XPATH, '//a[@href="/sample-page/2"]')   # WebElement
        Page2_menu.click()
 
        title=self.get_element(
            By.XPATH, '//div[@class="page-page text-center my-5"]/h1'
        ).text
        self.assertEqual(title, expectedTitle)
       

if __name__ == '__main__':
    unittest.main()  # (verbosity=4)