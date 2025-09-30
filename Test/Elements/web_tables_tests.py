import time

from Pages.Elements.web_tables_page import WebTablePage
from conftests import driver

class TestWebTable:

    def test_add_person(self, driver):
        web_table_page = WebTablePage(driver)
        web_table_page.open()

        new_person = web_table_page.add_person()
        table_result = web_table_page.check_added_person()

        assert new_person in table_result

    def test_search_person(self, driver):
        web_table_page = WebTablePage(driver)
        web_table_page.open()




    def test_edit_person(self, driver):
        web_table_page = WebTablePage(driver)
        web_table_page.open()




