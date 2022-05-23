from time import sleep
from unicodedata import name
from pages.BasePage import BasePage
from pages.Locators import TodoPageLocators

class TodoPage(BasePage):
    
    def get_title(self):
        return self.get_element(TodoPageLocators.Title).text

    def add_item(self, item):
        name_input = self.get_element(TodoPageLocators.AddItemInput)
        name_input.clear()
        name_input.send_keys(item)
 
        btn = self.get_element(TodoPageLocators.AddItemButton)
        btn.click()

    def get_item_from_pending_list_by_name(self, item):
        return self.get_element(TodoPageLocators.get_item_from_list(1, item))
    
    def get_item_from_ongiong_list_by_name(self, item):
        return self.get_element(TodoPageLocators.get_item_from_list(2, item))
    
    def get_item_from_completed_list_by_name(self, item):
        return self.get_element(TodoPageLocators.get_item_from_list(3, item))

    def remove_item_from_pending_list_by_name(self, item):
        btn = self.get_element(TodoPageLocators.get_remove_button_from_list(1, item))
        btn.click()

    def get_items_from_pending_list_by_name(self, item):
        return self.driver.find_elements(*TodoPageLocators.get_item_from_list(1, item))

    def get_items_from_completed_list_by_name(self, item):
        return self.driver.find_elements(*TodoPageLocators.get_item_from_list(3, item))

    def move_from_pending_to_ongiong(self, item):
        next_btn = self.get_clickable_element(TodoPageLocators.get_next_status_button(1, item))
        next_btn.click()
        sleep(1)

    def move_from_ongiong_to_completed(self, item):
        next_btn = self.get_clickable_element(TodoPageLocators.get_next_status_button(2, item))
        next_btn.click()
        sleep(1)
