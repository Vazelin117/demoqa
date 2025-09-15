from Locators.Elements.text_box_locators import TextBoxLocators
from Pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    full_name = "Иван иванов"
    email = "Vazelin117@gmail.com"
    current_address = "д. Нижние подзалупки, ул. какая-то, д.2"
    permanent_address = current_address

    def fill_all_fields(self):
        self.is_element_visible(self.locators.FULL_NAME).send_keys(self.full_name)
        self.is_element_visible(self.locators.EMAIL).send_keys(self.email)
        self.is_element_visible(self.locators.CURRENT_ADDRESS).send_keys(self.current_address)
        self.is_element_visible(self.locators.PERMANENT_ADDRESS).send_keys(self.permanent_address)
        self.click(self.locators.SUBMIT)

    def get_filled_text(self):
        filled_full_name = self.is_element_visible(self.locators.FILLED_NAME).text
        filled_email = self.is_element_visible(self.locators.FILLED_EMAIL).text
        filled_current_address = self.is_element_visible(self.locators.FILLED_CURRENT_ADDRESS).text
        filled_permanent_address = self.is_element_visible(self.locators.FILLED_PERMANENT_ADDRESS).text
        return filled_full_name, filled_email, filled_current_address, filled_permanent_address

