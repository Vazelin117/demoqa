from selenium.webdriver.common.by import By

class WebTableLocators:
    #Строка в таблице
    FULL_PEOPLE_LIST = (By.XPATH, '//div[@role="rowgroup"]')


    ADD_BTN = (By.XPATH, '//button[@id="addNewRecordButton"]')

    #Локаторы в модалке
    FIRST_NAME_FLD = (By.XPATH, '//input[@id="firstName"]')
    LAST_NAME_FLD = (By.XPATH, '//input[@id="lastName"]')
    EMAIL_FLD = (By.XPATH, '//input[@id="userEmail"]')
    AGE_FLD = (By.XPATH, '//input[@id="age"]')
    SALARY_FLD = (By.XPATH, '//input[@id="salary"]')
    DEPARTMENT_FLD = (By.XPATH, '//input[@id="department"]')

    SUBMIT_BTN = (By.XPATH, '//button[@id="submit"]')

    #Поле поиска
    TYPE_TO_SEARCH_FIELD = (By.XPATH, "//div[@class='rt-tr -odd']/div[@class='rt-td' and not(div[@class='action-buttons'])]")

    #Кнопка редактирования записи
    def edit_record_btn(self, record_num):
        locator_value = f'//span[@id="edit-record-{record_num}"]'
        final_locator = (By.XPATH, locator_value)
        return final_locator

    #Кнопка удаления записи
    def delete_record_btn(self, record_num):
        locator_value = f'//id[@id="delete-record-{record_num}"]'
        final_locator = (By.XPATH, locator_value)
        return final_locator
