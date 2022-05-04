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
email = os.environ['EMAIL']
expectedTitle= "We sent you an email."

class ResetPasswordTest(BaseTestCase):
    """
    ID: 018
    Scenariusz: Otrzymanie emaila z linkiem do resetu hasła
    """
    def test_reset_pasword_successfull(self):
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Login”
        sign_in_link = driver.find_element(
            By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        
       #  2.Kliknij w opcje ”przypomnij hasło”
        click_forgot_password = driver.find_element(
           By.XPATH, '//a[@href="/find-password"]')
        click_forgot_password.click()
       # 3. Wpisz adres email w polu „znajdź hasło”
        email_input = driver.find_element(By.ID, "input-email")
        email_input.send_keys(email)
       # 4.Kliknij „żadanie nowego hasła”
        request_new_password_btn = driver.find_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        request_new_password_btn.click()
        #5. Assercja  "request new email"- assercja potwierdzenia wysłania emaila (z linkiem do zmiany hasła)
        title=driver.find_element(
            By.XPATH, '//div[@class="card-body"]/h1'
        ).text
        self.assertEqual(title, expectedTitle)
        # 6. Sprawdź skrzynkę emailową pod adresem http://127.0.0.1:8025
        driver.get(os.environ['MAILHOG_URL'])
        sleep(1)
        # 7. Otwórz email "reset hasła"
        email_reset = driver.find_element(
            By.XPATH, '//div[@class="messages container-fluid ng-scope"]/div[1]')  # WebElement
        email_reset.click()
        sleep(1)
        #8. Assercja-klawisz resetu hasła
        iframe = driver.find_element(By.ID, "preview-html")
        driver.switch_to.frame(iframe)
        reset_password_btn = driver.find_element(
            By.XPATH, '//a[contains(text(), "Reset your password")]')  # WebElement
        reset_password_btn.click()
        driver.switch_to.default_content()


if __name__ == '__main__':
    unittest.main()  # (verbosity=4)
