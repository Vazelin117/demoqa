from Data.Elements.check_box_data import CheckBoxData
from Locators.Elements.check_box_locators import CheckBoxLocators
from Pages.base_page import BasePage


class CheckBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/checkbox")
        self.driver = driver

    locators = CheckBoxLocators()
    data_to_locators = CheckBoxData()

    def expand_all_buttons_manually(self):
        find_locator = CheckBoxLocators()
        for i in range(1, 7):
            self.click(find_locator.expand_collapse_btns(i))

    def collapse_all_buttons_manually(self):
        find_locator = CheckBoxLocators()
        self.expand_all_buttons_manually()
        for i in range(6, 0, -1):
            self.click(find_locator.expand_collapse_btns(i))





    def expand_all(self):
        return

    def collapse_all(self):
        return

    def select_all_checkboxes(self):
        return


