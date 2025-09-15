import time
from Pages.Elements.text_box_page import TextBoxPage
from Pages.start_page import StartPage
from Locators.strat_page_locators import  StartPageLocators
from conftests import driver

#тест на наличие/отсутствие плейсхолдера

class TestElements:

    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()

            text_box_page.fill_all_fields()
            print(text_box_page.get_filled_text())






