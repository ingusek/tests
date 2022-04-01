# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

    def testMoveItemFromPendingToOngoing(self):
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Login”
        # Szukam elementu
        # self.driver.find_element_by_partial_link_text("Login") # Selenium 3
        # Metoda find_element zwraca instancję klasy WebElement
        sign_in_link = driver.find_element(
            By.PARTIAL_LINK_TEXT, "Login")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpsz unikalną nazwę użytkownika”
        login_input = driver.find_element(By.ID, "input-username")
        login_input.send_keys(login)
        # 3. Wpisz hasło
        password_input = driver.find_element(By.ID, "input-password")
        password_input.send_keys(password)
        # 4. Kliknij Login
        login_btn = driver.find_element(
            By.XPATH, '//button[@type="submit"]')  # WebElement
        login_btn.click()
        sleep(1)
        # 5. Kliknięcie w zakładkę "Todo"
        Todo_btn = driver.find_element(
            By.XPATH, '//a[@href="/frontend-vue/todo"]')
        Todo_btn.click()

        # 6. Wyświetlenie pola TodoApp
        sleep(5)
        title = driver.find_element(By.TAG_NAME, 'h1').text
        expectedTitle = "Todo App"
        self.assertEqual(title, expectedTitle)

        name_input = driver.find_element(By.ID, "input-name")
        name_input.send_keys("śniadanie")

        # 7. Kliknij Add
        Add_btn = driver.find_element(
            By.XPATH, '//form//button[@type="submit"]')  # WebElement
        Add_btn.click()

       # 8. Przeniesienie pozycji z listy Pending  do listy Ongoing
       # Przenies_element = driver.find_element(
       # By.XPATH, '//div[@class="l-2 todo-ongoing-span"][1]')  # WebElement
       # Przenies_element.send_keys("śniadanie")
        sleep(1)
        source = driver.find_element(
            By.XPATH, '//div[@data-name="todo-pending-list-0"]')
        target = driver.find_element(
            By.XPATH, '//div[@class="card-deck"]//div[@class="card mb-3"][2]//div[@class="todo-list-group"]')
        actions2 = ActionChains(driver)
        # actions2.drag_and_drop(
        #     source, target).perform()
        actions2.click_and_hold(source).move_to_element(target).pause(2).move_by_offset(20, 20).pause(2).release().perform()
        # sleep(5)

        # self.assertEqual(source.text, target.text)
        sleep(5)

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=4)
