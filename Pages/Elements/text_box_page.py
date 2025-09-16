from Generator.generator import generate_person
from Locators.Elements.text_box_locators import TextBoxLocators
from Pages.base_page import BasePage


class TextBoxPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/text-box")
        self.driver = driver

    locators = TextBoxLocators()

    person_info = next(generate_person()) #next дает лишь одну итерацию от generate_person()
    full_name = person_info.full_name
    email = person_info.email
    current_address = person_info.current_address.replace('\n', ' ')
    permanent_address = person_info.permanent_address.replace('\n', ' ')



    def fill_all_fields(self):
        self.is_element_visible(self.locators.FULL_NAME).send_keys(self.full_name)
        self.is_element_visible(self.locators.EMAIL).send_keys(self.email)
        self.is_element_visible(self.locators.CURRENT_ADDRESS).send_keys(self.current_address)
        self.is_element_visible(self.locators.PERMANENT_ADDRESS).send_keys(self.permanent_address)
        self.click(self.locators.SUBMIT)

    def get_filled_text(self):
        filled_full_name = self.is_element_visible(
            self.locators.FILLED_NAME).text.split(":")[1]

        filled_email = self.is_element_visible(
            self.locators.FILLED_EMAIL).text.split(":")[1]

        filled_current_address = self.is_element_visible(
            self.locators.FILLED_CURRENT_ADDRESS).get_attribute("innerText").split(":")[1]

        filled_permanent_address = self.is_element_visible(
            self.locators.FILLED_PERMANENT_ADDRESS).get_attribute("innerText").split(":")[1]

        return filled_full_name, filled_email, filled_current_address, filled_permanent_address

