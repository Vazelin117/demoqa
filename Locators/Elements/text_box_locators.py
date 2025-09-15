from selenium.webdriver.common.by import By

class TextBoxLocators:

    #Поля для заполнения

    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    #Заполненные поля

    FILLED_NAME = (By.XPATH, '//p[@id="name"]')
    FILLED_EMAIL = (By.XPATH, '//p[@id="email"]')
    FILLED_CURRENT_ADDRESS = (By.XPATH, '//p[@id="currentAddress"]')
    FILLED_PERMANENT_ADDRESS = (By.XPATH, '//p[@id="permanentAddress"]')