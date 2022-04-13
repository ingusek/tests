from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_element(self, locator):
        WebDriverWait(self.driver, 100).until(lambda driver: driver.find_element(*locator))
        return self.driver.find_element(*locator)
