from selenium.webdriver.common.by import By

class CheckBoxLocators:

    EXPAND_COLLAPSE_BTN = (By.XPATH, '//button[@aria-label="Toggle"]')

    EXPAND_ALL_BTN = (By.XPATH, '//button[@aria-label="Expand all"]')
    COLLAPSE_ALL_BTN = (By.XPATH, '//button[@aria-label="Collapse all"]')

    def expand_collapse_btns(self, btn_num):
        locator_type, locator_value = self.EXPAND_COLLAPSE_BTN
        final_locator = (locator_type, f"({locator_value})[{btn_num}]")
        return final_locator


    #locator брать из CheckBoxData
    def check_box_locators(self, locator):
        final_locator = f'//label[@for="tree-node-{locator}]"]/span[@class = "rct-checkbox"]'
        return final_locator



