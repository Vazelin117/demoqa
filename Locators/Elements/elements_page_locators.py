from selenium.webdriver.common.by import By


class ElementsPageLocators:

    #Elements
    TEXT_BOX = (By.XPATH, '//span[contains(text(), "Text Box")]')
    CHECK_BOX = (By.XPATH, '//span[contains(text(), "Check Box")]')
    RADIO_BUTTON = (By.XPATH, '//span[contains(text(), "Radio Button")]')
    WEB_TABLES = (By.XPATH, '//span[contains(text(), "Web Tables")]')
    BUTTONS = (By.XPATH, '//span[contains(text(), "Buttons")]')
    LINKS = (By.XPATH, '//span[contains(text(), "Links")]')
    BROKEN_LINKS_IMAGES = (By.XPATH, '//span[contains(text(), "Broken Links - Images")]')
    UPLOAD_AND_DOWNLOAD = (By.XPATH, '//span[contains(text(), "Upload and Download")]')
    DYNAMIC_PROPERTIES = (By.XPATH, '//span[contains(text(), "Dynamic Properties")]')