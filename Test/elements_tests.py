import time
from Pages.start_page import StartPage
from conftests import driver


def test_open_checkbox_page(driver):
    page = StartPage(driver)
    page.open()
    time.sleep(3600)


