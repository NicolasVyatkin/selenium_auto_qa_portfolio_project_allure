'''Configurating module'''
from datetime import datetime

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome. service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    """function that adds driver"""
    driver_service = Service(ChromeDriverManager().install())
    driver_chrome = webdriver.Chrome(service=driver_service)
    driver_chrome.maximize_window()
    yield driver_chrome
    attach = driver.get_screenshot_as_png()
    allure.attach(
        attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver_chrome.quit()
