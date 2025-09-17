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
        self.click(find_locator.expand_collapse_btns(1))
        self.click(find_locator.expand_collapse_btns(2))
        self.click(find_locator.expand_collapse_btns(3))
        self.click(find_locator.expand_collapse_btns(4))
        self.click(find_locator.expand_collapse_btns(5))
        self.click(find_locator.expand_collapse_btns(6))

    def collapse_all_buttons_manually(self):
        find_locator = CheckBoxLocators()
        self.expand_all_buttons_manually()

        self.click(find_locator.expand_collapse_btns(6))
        self.click(find_locator.expand_collapse_btns(5))
        self.click(find_locator.expand_collapse_btns(4))
        self.click(find_locator.expand_collapse_btns(3))
        self.click(find_locator.expand_collapse_btns(2))
        self.click(find_locator.expand_collapse_btns(1))





    def expand_all(self):
        return

    def collapse_all(self):
        return

    def select_all_checkboxes(self):
        return


