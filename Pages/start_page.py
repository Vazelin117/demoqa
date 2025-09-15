from selenium.webdriver.common.by import By
from .base_page import BasePage

class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/")
        self.driver = driver

    def open(self):
        self.driver.get(self.url)