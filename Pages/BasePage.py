from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = url

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=f"Element {locator} not found")

    def is_element_selected(self, locator):
        return self.wait.until(EC.element_to_be_selected(locator))

    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.presence_of_element_located(locator),
                        message=f"Element {locator} not found").click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator).text
        return element


