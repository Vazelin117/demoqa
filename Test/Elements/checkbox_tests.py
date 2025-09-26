import time
from Pages.Elements.check_box_page import CheckBoxPage
from Data.Elements.check_box_data import CheckBoxData
from conftests import driver


class TestCheckBoxPage:

    class TestToggles:
        def test_expand_all_toggles_manual(self, driver):
            assert_data = CheckBoxData()
            checkbox_page = CheckBoxPage(driver)
            checkbox_page.open()

            checkbox_page.expand_all_buttons_manually()
            assert checkbox_page.get_all_nesting_texts() == assert_data.EXPAND_DATA

        def test_collapse_toggles_manual(self, driver):
            assert_data = CheckBoxData()
            checkbox_page = CheckBoxPage(driver)
            checkbox_page.open()

            checkbox_page.expand_all_buttons_manually()
            checkbox_page.collapse_all_buttons_manually()
            assert checkbox_page.get_all_nesting_texts() != assert_data.EXPAND_DATA

        def test_click_expand_all_btn(self, driver):
            checkbox_page = CheckBoxPage(driver)
            assert_data = CheckBoxData()
            checkbox_page.open()

            checkbox_page.expand_all_btn()
            assert checkbox_page.get_all_nesting_texts() == assert_data.EXPAND_DATA

        def test_click_collapse_all_btn(self, driver):
            checkbox_page = CheckBoxPage(driver)
            assert_data = CheckBoxData()
            checkbox_page.open()

            checkbox_page.collapse_all_btn()
            assert checkbox_page.get_all_nesting_texts() != assert_data.EXPAND_DATA

        class TestCheckboxes:

            def test_select_checkboxes(self, driver):
                checkbox_page = CheckBoxPage(driver)
                checkbox_page.open()

                checkbox_page.click_random_checkbox()
                time.sleep(5)