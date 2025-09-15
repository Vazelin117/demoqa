import time
from Pages.start_page import StartPage
from Locators.strat_page_locators import  StartPageLocators
from conftests import driver

#тест на наличие заголовка
#тест на наличие/отсутствие плейсхолдера

def test_open_elements_page(driver):
    page = StartPage(driver)
    locators = StartPageLocators()
    page.open()
    page.click(locators.ELEMENTS)
    time.sleep(3600)


