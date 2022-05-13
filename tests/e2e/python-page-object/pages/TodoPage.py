from pages.BasePage import BasePage
from pages.Locators import TodoPageLocators

class TodoPage(BasePage):
    
    def get_title(self):
        return self.get_element(TodoPageLocators.Title).text
