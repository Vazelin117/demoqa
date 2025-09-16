from Pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/")
        self.driver = driver


    def get_text(self, locator):
        text = self.driver.find_element(*locator).text
        return text