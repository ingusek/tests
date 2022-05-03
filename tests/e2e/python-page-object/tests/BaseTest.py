from pages.HomePage import HomePage
from tests.TestData import TestData

from selenium import webdriver
import unittest

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        self.driver.implicitly_wait(0)

        # Stworzyć instancję klasy HomePage
        # Aby uzyskać dostęp do mechanizmów tej strony
        self.home_page = HomePage(self.driver)
        self.test_data = TestData()

    def tearDown(self):
        self.driver.quit()
