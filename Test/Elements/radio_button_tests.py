import time

from Pages.Elements.radio_button_page import RadioButtonPage
from conftests import driver

class TestRadioButton:

    def test_select_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver)
        radio_button_page.open()

        radio_button_page.select_radio_button("yes")
        output_yes = radio_button_page.get_output_result()
        assert output_yes == "Yes"

        radio_button_page.select_radio_button("impressive")
        output_impressive = radio_button_page.get_output_result()
        assert output_impressive == "Impressive"

        radio_button_page.select_radio_button("no")
        output_no = radio_button_page.get_output_result()
        assert output_no == "No"