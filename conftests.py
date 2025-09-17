import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os



def kill_chromedriver_processes():
    os.system("taskkill /f /im chromedriver.exe /t 2>nul")


@pytest.fixture(scope="function")
def driver():

    service = Service(executable_path=r"C:/Users/vazel/OneDrive/Рабочий стол/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver

    driver.quit()
    kill_chromedriver_processes()




