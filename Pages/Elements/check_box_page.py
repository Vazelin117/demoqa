from selenium.common import NoSuchElementException

from Data.Elements.check_box_data import CheckBoxData
from Locators.Elements.check_box_locators import CheckBoxLocators
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/checkbox")
        self.driver = driver

    locators = CheckBoxLocators()
    data_to_locators = CheckBoxData()

    #Раскрывает все вложенности сверху вниз
    def expand_all_buttons_manually(self):
        find_locator = CheckBoxLocators()
        for i in range(1, 7):#Я не знаю как посчитать количество, которое с каждым циклом увеличивается
                             #О, у меня же есть Expand all
            self.click(find_locator.expand_collapse_btns(i))

    #Закрывает все открытые вложенности снизу вверх
    def collapse_all_buttons_manually(self):
        find_locator = CheckBoxLocators()
        for i in range(6, 0, -1): #Я не знаю как посчитать количество, которое с каждым циклом увеличивается
                                  #О, у меня же есть Expand all
            self.click(find_locator.expand_collapse_btns(i))

    #Получить текст всех вложенностей после раскрытия. Вызывать после expand_all_buttons_manually
    def get_all_nesting_texts(self):
        find_locator = CheckBoxLocators()
        nesting_texts = []
        for i in range(1, self.nesting_text_count() + 1):
            final_locator = find_locator.get_nesting_text(i)
            element = self.driver.find_element(*final_locator)
            nesting_texts.append(element.text)
        return nesting_texts

    #Получить число тогглов для закрытия. Используется в get_all_nesting_texts
    def nesting_text_count(self):
        find_locator = CheckBoxLocators()
        text_count = len(self.find_elements(find_locator.NESTING_TEXT))
        return text_count




    def expand_all_btn(self):
        find_locator = CheckBoxLocators()
        self.click(find_locator.EXPAND_ALL_BTN)

    def collapse_all_btn(self):
        find_locator = CheckBoxLocators()
        self.expand_all_btn()
        self.click(find_locator.COLLAPSE_ALL_BTN)

    def select_all_checkboxes(self):
        return


