from selenium.webdriver.common.by import By

class StartPageLocators:

    #Входной параметр брать из StartPageData

    #Элементы на главной странице
    def get_locator(self, locator):
        locator = (By.XPATH, f"//h5[contains(text(), '{locator}')]")
        return locator

    # Элементы после перехода с главной страницы
    def get_locator_after_transit(self, locator):
        locator = (By.XPATH, f'//div[contains(text(), "{locator}")]/ancestor::span[@class="group-header"]'
                                           '/following-sibling::div[@class="element-list collapse show"]')
        return locator
