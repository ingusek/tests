# Import bibliotek
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import unittest
import os

# DANE TESTOWE
login = os.environ['LOGIN']
password = os.environ['PASSWORD']

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # Przygotowanie testu
        # Warunki wstępne testu
        # Otwarcie przeglądarki
        self.driver =  webdriver.Chrome()
        # Otwarcie strony
        self.driver.get(os.environ['APP_URL'])
        # Maksymalizacja okna
        self.driver.maximize_window()
        # Ustawienie bezwarunkowego czekania na elementy przy wyszukiwaniu
        # maks. 10 sekund
        self.driver.implicitly_wait(10)
        self.fake = Faker()
        
    def get_element(self, type, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((type, locator))
        )

    def get_clickable_element(self, type, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((type, locator))
        )
    

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()
