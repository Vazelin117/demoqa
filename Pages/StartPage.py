from selenium.webdriver.common.by import By
from .BasePage import BasePage

class StartPage(BasePage):
    CHECKBOXES = (By.ID, 'checkboxes')
    DROPDOWN = (By.ID, 'dropdown')

    def __init__(self, driver):
        super().__init__(driver, "https://the-internet.herokuapp.com/")
        self.driver = driver

    def open(self):
        self.driver.get(self.url)