import time
from Pages.Elements.check_box_page import CheckBoxPage
from conftests import driver


class TestCheckBoxPage:

    class TestToggles:
        def test_expand_all_toggles(self, driver):
            checkbox_page = CheckBoxPage(driver)
            checkbox_page.open()

            checkbox_page.expand_all_buttons_manually()

            time.sleep(5)

        def test_collapse_toggles(self, driver):
            checkbox_page = CheckBoxPage(driver)
            checkbox_page.open()

            checkbox_page.collapse_all_buttons_manually()

            time.sleep(5)


