import time
from Pages.BasePage import BasePage
from Pages.StartPage import StartPage
from conftests import driver


def test(driver):
    page = StartPage(driver)
    page.open()
    time.sleep(3600)
