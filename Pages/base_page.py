from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    from selenium.webdriver import Chrome as WebDriver, ActionChains
except ImportError:
    from selenium import webdriver
    WebDriver = webdriver.Chrome

class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=f"Element {locator} not found")

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_element_selected(self, locator):
        return self.wait.until(EC.element_to_be_selected(locator),
                               message=f"Element {locator} not found")

    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator),
                               message=f"Element {locator} not found")

    def is_elements_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator),
                               message=f"Element {locator} not found")

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

    def get_texts(self, locator):
        elements = self.find_elements(locator)
        return elements

    def go_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()


