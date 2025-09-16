from Data.start_page_data import StartPageData
from Locators.strat_page_locators import StartPageLocators
from Pages.start_page import StartPage
from conftests import driver


class TestStartPage:

    def test_start_page(self, driver):
        start_page = StartPage(driver)
        asserted_data = StartPageData()

        start_page.open()

        assert asserted_data.ELEMENTS
        assert asserted_data.ALERTS
        assert asserted_data.FORMS
        assert asserted_data.WIDGETS
        assert asserted_data.INTERACTIONS
        assert asserted_data.BOOK_STORE

    def test_after_elements(self, driver):
        start_page = StartPage(driver)
        start_page_locators = StartPageLocators()
        start_page_data = StartPageData()

        start_page.open()
        start_page.click(start_page_locators.get_locator(start_page_data.ELEMENTS))

        assert start_page_locators.get_locator_after_transit(start_page_data.ELEMENTS)

    def test_after_forms(self, driver):
        start_page = StartPage(driver)
        start_page_locators = StartPageLocators()
        start_page_data = StartPageData()

        start_page.open()
        start_page.click(start_page_locators.get_locator(start_page_data.FORMS))

        assert start_page_locators.get_locator_after_transit(start_page_data.FORMS)