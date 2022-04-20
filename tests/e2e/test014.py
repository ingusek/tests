# Import bibliotek
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop
from faker import Faker
from time import sleep
import unittest
import os

# DANE TESTOWE
login = os.environ['LOGIN']
password = os.environ['PASSWORD']

class RegistrationTest(unittest.TestCase):
    """
    Scenariusz : Zmiana statusu z Pending na Ongoing
    """

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

    def get_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def get_clickable_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
    
    def testMoveItemFromPendingToOngoing(self):
        # Faktyczny test
        driver = self.driver

        # 1. Strona logowania
        sign_in_link = self.get_element((By.PARTIAL_LINK_TEXT, "Login"))  # Selenium 4
        sign_in_link.click()

        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = self.get_element((By.ID, "input-username"))
        login_input.send_keys(login)

        # 3. Wpisz hasło
        password_input = self.get_element((By.ID, "input-password"))
        password_input.send_keys(password)

        # 4. Kliknij Login
        login_btn = self.get_element((By.XPATH, '//button[@type="submit"]'))  # WebElement
        login_btn.click()

        sleep(1)

        # 5. Kliknięcie w zakładkę "Todo"
        todo_btn = self.get_element((By.XPATH, '//a[@href="/frontend-vue/todo"]'))
        todo_btn.click()

        # # 6. Wyświetlenie pola TodoApp
        # title = self.get_element((By.TAG_NAME, 'h1')).text
        # expectedTitle = "Todo App"
        # self.assertEqual(title, expectedTitle)

        name_input = self.get_element((By.ID, "input-name"))
        name_input.send_keys("śniadanie")

        # 7. Kliknij Add
        Add_btn = self.get_element((By.XPATH, '//form//button[@type="submit"]'))  # WebElement
        Add_btn.click()

        # source = self.get_clickable_element((By.XPATH, '//div[@data-name="todo-pending-list-0"]'))
        # target = self.get_clickable_element((By.XPATH, '//div[@class="card-deck"]//div[@class="card mb-3"][2]//div[@class="todo-list-group"]'))
        source = self.get_clickable_element((By.CSS_SELECTOR, 'div[data-name=todo-pending-list-0]'))
        target = self.get_clickable_element((By.CSS_SELECTOR, 'div.card-deck div.card:nth-child(2) div.todo-list-group'))
        
        actions2 = ActionChains(driver)
        actions2.drag_and_drop(
             source, target).perform()
        
        
        # actions2.click_and_hold(source).pause(10).move_to_element(target).double_click().pause(10).move_by_offset(180, 180).pause(10).release().perform()
        # sleep(5)

        # self.assertEqual(source.text, target.text)
        sleep(5)

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=6)
