from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_element(self, locator):
        element_present = EC.presence_of_element_located(locator)
        WebDriverWait(self.driver, 100).until(element_present)
        return self.driver.find_element(*locator)

    def get_element_with_text(self, locator, text):
        element_present = EC.text_to_be_present_in_element(locator, text)
        WebDriverWait(self.driver, 100).until(element_present)
        return self.driver.find_element(*locator)

    def get_clickable_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

    def switch_to_frame(self, locator):
        iframe = self.get_element(locator)
        self.driver.switch_to.frame(iframe)

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
