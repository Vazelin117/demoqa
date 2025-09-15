from selenium.webdriver.common.by import By

class StartPageLocators:
    ELEMENTS = (By.XPATH, "//h5[contains(text(), 'Elements')]")
    FORMS = (By.XPATH, "//h5[contains(text(), 'Forms')]")
    ALERTS = (By.XPATH, "//h5[contains(text(), 'Alerts')]")
    WIDGETS = (By.XPATH, "//h5[contains(text(), 'Widgets')]")
    INTERACTIONS = (By.XPATH, "//h5[contains(text(), 'Interactions')]")
    BOOK_STORES = (By.XPATH, "//h5[contains(text(), 'Book Store Application')]")