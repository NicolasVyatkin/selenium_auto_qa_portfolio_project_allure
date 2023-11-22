import os
import allure
from generator.generator import generated_file, generated_person, generated_subject
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class FormPage(BasePage):

    locators = FormPageLocators()

    @allure.step('fill in all fields')
    def fill_form_fields(self):
        # next - creates only one person
        person = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(
            self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(
            self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(
            self.locators.SUBJECT).send_keys(generated_subject())
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(
            person.current_address)
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(
            self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(
            self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person

    @allure.step('get form result')
    def from_result(self):
        """function that saves data to the list"""
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]

        # for i in result_list:
        #     result_text.append(i.text)

        return result_text
