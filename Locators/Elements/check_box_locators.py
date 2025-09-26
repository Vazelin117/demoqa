from selenium.webdriver.common.by import By

class CheckBoxLocators:

    EXPAND_COLLAPSE_BTN = (By.XPATH, '//button[@aria-label="Toggle"]')
    NESTING_TEXT = (By.XPATH, '//span[@class="rct-title"]')

    EXPAND_ALL_BTN = (By.XPATH, '//button[@aria-label="Expand all"]')
    COLLAPSE_ALL_BTN = (By.XPATH, '//button[@aria-label="Collapse all"]')

    VISIBLE_ITEMS = (By.XPATH, '//span[@class="rct-title"]')
    SELECTED_ITEMS = (By.XPATH, '//span[@class="text-success"]')

    CHECKED_CHECKBOXES = (By.XPATH, '//span[@class="rct-text"]//*[@class="rct-icon rct-icon-check"]')
    HALF_CHECKED_CHECKBOXES = (By.XPATH, '//span[@class="rct-text"]//*[@class="rct-icon rct-icon-half-check"]')
    UNCHECKED_CHECKBOXES = (By.XPATH, '//span[@class="rct-text"]//*[@class="rct-icon rct-icon-uncheck"]')

    def expand_collapse_btns(self, btn_num):
        locator_type, locator_value = self.EXPAND_COLLAPSE_BTN
        final_locator = (locator_type, f"({locator_value})[{btn_num}]")
        return final_locator

    #Локатор выбора чекбокса. locator брать из CheckBoxData.EXPAND_DATA
    def check_box_locator(self, locator):
        final_locator = f'//label[@for="tree-node-{locator}]"]/span[@class = "rct-checkbox"]'
        return final_locator

    #Получить локатор с вложенным текстом
    def get_nesting_text(self, nest_num):
        locator_type, locator_value = self.NESTING_TEXT
        final_locator = (locator_type, f'({locator_value})[{nest_num}]')
        return final_locator



