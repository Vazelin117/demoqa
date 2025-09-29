from Locators.Elements.radio_button_locators import  RadioButtonLocators
from Pages.base_page import BasePage


class RadioButtonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/radio-button")
        self.driver = driver

    def select_radio_button(self, choice):
        radio_button_locators = RadioButtonLocators()
        choices = {'yes': radio_button_locators.YES_RADIO_BTN,
                  'impressive': radio_button_locators.IMPRESSIVE_RADIO_BTN,
                  'no': radio_button_locators.NO_RADIO_BTN}
        self.click(choices[choice])


    def get_output_result(self):
        radio_button_locators = RadioButtonLocators()

        return self.find_element(radio_button_locators.OUTPUT_RESULT).text