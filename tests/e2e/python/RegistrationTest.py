# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from BaseTestCase import BaseTestCase
from faker import Faker
from time import sleep
import unittest
import os

invalid_email = "ji8989898uii"

class RegistrationTest(BaseTestCase):
    
    """
    Scenariusz : Rejestracja nowego użytkownika w systemie
    """
    def test_registration_success(self):
        email = self.fake.email()
        password = self.fake.password()
        login = self.fake.simple_profile()['username']
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
  
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Sign up”
        sign_in_link = self.get_element(
            By.PARTIAL_LINK_TEXT, "Sign up")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpisz e-mail
        # Znajdź element
        email_input = self.get_element(By.ID, "input-email")
        # Zastosuj metodę send_keys() żeby wpisać coś w element
        email_input.send_keys(email)
        # 3. Wpsz unikalną nazwę użytkownika”
        login_input = self.get_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 4. Wpisz hasło
        password_input = self.get_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 5. Wpisz imię
        firstname_input = self.get_element(By.ID, "input-first-name")
        firstname_input.send_keys(first_name)
        # 6. Wpisz nazwisko
        lastname_input = self.get_element(By.ID, "input-last-name")
        lastname_input.send_keys(last_name)
        # 7. Kliknij Register
        register_btn = self.get_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()

        # 8. Sprawdzenie rejestracji użytkownika
        sleep(1)
        title = self.get_element(By.TAG_NAME, 'h1').text
        expectedTitle = "You are successfully registered."
        self.assertEqual(title, expectedTitle)
        # 9. Przejście na stronę potwierdzenia emaila
        driver.get(os.environ['MAILHOG_URL'])
        sleep(1)
        # 10. Otwarcie emaila
        email_link = self.get_element(
            By.XPATH, '//div[@class="messages container-fluid ng-scope"]/div[1]')  # WebElement
        email_link.click()
        sleep(1)

        iframe = self.get_element(By.ID, "preview-html")
        driver.switch_to.frame(iframe)
        confirm_email_url = self.get_element(
            By.PARTIAL_LINK_TEXT, 'Confirm')
        confirm_email_url.click()

        driver.switch_to.window(driver.window_handles[1])
  
        # 11. Sprawdzenie przeniesienia na strone logowania
        titleLogin = self.get_element(By.XPATH, '//div[@class="card-body"]/h1').text
        expectedTitleLogin = "Login"
        self.assertEqual(titleLogin, expectedTitleLogin)
        
    """
    Scenariusz: Rejestracja z niepoprawnym adresem e-mail
    """
    def test_registeration_with_invalid_email(self):
        password = self.fake.password()
        login = self.fake.simple_profile()['username']
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()

        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Sign up”
        # Szukam elementu
        # Metoda find_element zwraca instancję klasy WebElement
        sign_in_link = self.get_element(
            By.PARTIAL_LINK_TEXT, "Sign up")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpisz niepoprawny e-mail
        # Znajdź element
        email_input = self.get_element(By.ID, "input-email")
        # Zastosuj metodę send_keys() żeby wpisać coś w element
        email_input.send_keys(invalid_email)
        # 3. Wpsz unikalną nazwę użytkownika”
        login_input = self.get_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 4. Wpisz hasło
        password_input = self.get_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 5. Wpisz imię
        firstname_input = self.get_element(By.ID, "input-first-name")
        firstname_input.send_keys(first_name)
        # 6. Wpisz nazwisko
        lastname_input = self.get_element(By.ID, "input-last-name")
        lastname_input.send_keys(last_name)
        # 7. Kliknij Register
        register_btn = self.get_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()
        self.assertFalse(register_btn.is_enabled())


    """
    Scenariusz: Rejestracja z zajętym adresem e-mail
    """
    def test_registration_with_email_already_in_use(self):
        login = self.fake.simple_profile()['username']
        email = os.environ['EMAIL']
        password = os.environ['PASSWORD']
        first_name = "Inga"
        last_name = "Gajewska"
        # Faktyczny test
        driver = self.driver
        sign_in_link = self.get_element(
            By.PARTIAL_LINK_TEXT, "Sign up")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpisz niepoprawny e-mail
        # Znajdź element
        email_input = self.get_element(By.ID, "input-email")
        # Zastosuj metodę send_keys() żeby wpisać coś w element
        email_input.send_keys(email)
        # 3. Wpsz unikalną nazwę użytkownika”
        login_input = self.get_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 4. Wpisz hasło
        password_input = self.get_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 5. Wpisz imię
        firstname_input = self.get_element(By.ID, "input-first-name")
        firstname_input.send_keys(first_name)
        # 6. Wpisz nazwisko
        lastname_input = self.get_element(By.ID, "input-last-name")
        lastname_input.send_keys(last_name)
        # 7. Kliknij Register
        register_btn = self.get_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()
        # Oczekiwany rezultat
        # 8. Sprawdzenie czy pojawił się komunikat o zajętym adresie e-mail
        error_text = self.get_element(
            By.XPATH, '//div[@class="text-danger message-col col"]').text
        expectedError_text = "Email is already in use."
        self.assertEqual(error_text, expectedError_text)


    """
    Scenariusz: Rejestracja z zajętą nazwą użytkownika
    """
    def test_registration_with_username_already_in_use(self):
        email = self.fake.email()
        login = os.environ['LOGIN']
        password = os.environ['PASSWORD']
        first_name = "Inga"
        last_name = "Gajewska"
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Sign up”
        sign_in_link = self.get_element(
            By.PARTIAL_LINK_TEXT, "Sign up")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpisz niepoprawny e-mail
        # Znajdź element
        email_input = self.get_element(By.ID, "input-email")
        # Zastosuj metodę send_keys() żeby wpisać coś w element
        email_input.send_keys(email)
        # 3. Wpsz unikalną nazwę użytkownika”
        login_input = self.get_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 4. Wpisz hasło
        password_input = self.get_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 5. Wpisz imię
        firstname_input = self.get_element(By.ID, "input-first-name")
        firstname_input.send_keys(first_name)
        # 6. Wpisz nazwisko
        lastname_input = self.get_element(By.ID, "input-last-name")
        lastname_input.send_keys(last_name)
        # 7. Kliknij Register
        register_btn = self.get_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        register_btn.click()
        sleep(1)
        # Oczekiwany rezultat
        # 8. Sprawdzenie czy pojawił się komunikat o zajętym adresie e-mail
        error_text = self.get_element(
            By.XPATH, '//div[@class="text-danger message-col col"]').text
        expectedError_text = "Username is already in use."
        self.assertEqual(error_text, expectedError_text)

if __name__ == '__main__':
    unittest.main()  # (verbosity=4)
