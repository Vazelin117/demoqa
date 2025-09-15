import time
from Pages.Elements.text_box_page import TextBoxPage
from conftests import driver

#тест на наличие/отсутствие плейсхолдера

class TestElements:

    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()

            text_box_page.fill_all_fields()

            (filled_name, filled_email,
             filled_cur_addr, filled_per_addr) = text_box_page.get_filled_text()

            print(filled_name, filled_email, filled_per_addr)

            assert filled_name == text_box_page.full_name
            assert filled_email == text_box_page.email
            assert filled_cur_addr == text_box_page.current_address
            assert filled_per_addr == text_box_page.permanent_address






