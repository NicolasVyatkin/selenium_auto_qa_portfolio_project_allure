import time
import allure
from selenium.webdriver.common.keys import Keys
from locators.locator_google import FormPageLocators as Locators
from pages.base_page import BasePage


class FormGooglePage(BasePage):
    """class that worcks with curent page"""

    @allure.step('Fills search field and submit')
    def fill_fields_and_submit(self):
        """function that finds elements by locator and make a action"""

        some_input = 'generated_person'
        search_field = self.element_is_visible(Locators.SEARCH_FIELD)
        search_field.send_keys(some_input)
        time.sleep(2)
        search_field.send_keys(Keys.RETURN)
