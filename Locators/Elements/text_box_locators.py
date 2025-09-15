from selenium.webdriver.common.by import By

class TextBoxLocators:
    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//input[@id="CurrentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//input[@id="PermanentAddress"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')