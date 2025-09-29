from selenium.webdriver.common.by import By

class RadioButtonLocators:
    ALL_RADIO_BTN = (By.XPATH, '//div[contains(@class, "radio")]')
    ENABLED_RADIO_BTN = (By.XPATH, '//div[contains(@class, "custom-control custom-radio")]')
    DISABLED_RADIO_BTN = (By.XPATH, '//div[contains(@class, "disabled custom-radio")]')

    YES_RADIO_BTN = (By.XPATH, '//input[@id="yesRadio"]/..')
    IMPRESSIVE_RADIO_BTN = (By.XPATH, '//input[@id="impressiveRadio"]/..')
    NO_RADIO_BTN = (By.XPATH, '//input[@id="noRadio"]/..')

    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')