import random

from Generator.generator import generate_person
from Locators.Elements.web_tables_locators import WebTableLocators
from Pages.base_page import BasePage


class WebTablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/webtables')
        self.driver = driver

    locators = WebTableLocators()

    def add_person(self):
        person_count = random.randint(1, 3)
        while person_count != 0:
            self.click(self.locators.ADD_BTN)

            person_info = next(generate_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            self.is_element_visible(self.locators.FIRST_NAME_FLD).send_keys(first_name)
            self.is_element_visible(self.locators.LAST_NAME_FLD).send_keys(last_name)
            self.is_element_visible(self.locators.EMAIL_FLD).send_keys(email)
            self.is_element_visible(self.locators.AGE_FLD).send_keys(age)
            self.is_element_visible(self.locators.SALARY_FLD).send_keys(salary)
            self.is_element_visible(self.locators.DEPARTMENT_FLD).send_keys(department)

            self.is_element_visible(self.locators.SUBMIT_BTN).click()

            person_count -= 1

            return [first_name, last_name, str(age), email, str(salary), department]

    def check_added_person(self):
        person_list = self.is_elements_visible(self.locators.FULL_PEOPLE_LIST)
        data = []
        for i in person_list:
            data.append(i.text.splitlines())

        return data



