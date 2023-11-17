import base64
import os
import random
import allure
import requests
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import ButtonsPageLocators, CheckBoxPageLocatirs, DynamicPropertiesPageLocators, LinksPageLocators, RadioButtonPageLocators, TextBoxPageLocators, UploadAndDownloadPageLocators, WebTablePageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


class TextBoxPage(BasePage):
    """function that starts the test"""
    locators = TextBoxPageLocators()

    @allure.step("Fill in all fields")
    def fill_all_fields(self):
        # next - creates only one person
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_adress = person_info.current_address
        permanent_adress = person_info.permanent_address
        with allure.step('filing fields'):
            self.element_is_visible(
                self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(
                self.locators.EMAIL).send_keys(email)
            self.element_is_visible(
                self.locators.CURRENT_ADDRES).send_keys(current_adress)
            self.element_is_visible(
                self.locators.PERMANENT_ADRESS).send_keys(permanent_adress)
        with allure.step('click submit button'):
            self.element_is_visible(
                self.locators.SUBMIT).click()
        # time.sleep(5)
        return full_name, email, str(current_adress).replace('\n', ' '), str(permanent_adress).replace('\n', ' ')

    @allure.step('check filled form')
    def check_fielled_form(self):
        full_name = self.element_is_present(
            self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(
            self.locators.CREATED_EMAIL).text.split(':')[1]
        current_adress = self.element_is_present(
            self.locators.CREATED_CURRENT_ADDRES).text.split(':')[1]
        permanent_adress = self.element_is_present(
            self.locators.CREATED_PERMANENT_ADRESS).text.split(':')[1]
        current_adress_notn = current_adress.replace("\n", " ")
        permanent_adress_notn = permanent_adress.replace("\n", " ")
        # time.sleep(5)
        return full_name, email,  current_adress_notn, permanent_adress_notn


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocatirs()

    @allure.step('open full list')
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('click random items')
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step('get checked checkbox')
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []  # boofer for elements
        for box in checked_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(" ", "").replace('doc', '').replace('.', '').lower()

    @allure.step('get output result')
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    @allure.step('click on the radiobutton')
    def click_on_the_radio_button(self, choise):
        choises = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON, }
        radio = self.element_is_visible(choises[choise]).click()

    @allure.step('get output result')
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step('add new person')
    def add_new_person(self, count=1):
        '''function that creates new person'''
        count = random.randint(1, 3)
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.first_name
            lastname = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(
                self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(
                self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(
                self.locators.SALARY_INPYT).send_keys(salary)
            self.element_is_visible(
                self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

            # count -= 1
            # return firstname, lastname, email, age, salary, department

    @allure.step('check added people')
    def check_new_added_person(self):
        '''function that checks created person'''
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('find some person')
    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('check found person')
    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('update person information')
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    @allure.step('delete person')
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('check deleted person')
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('select up to some rows')
    def select_up_to_some_rows(self):
        self.remove_footer()
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(
                self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible(
                (By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('check count rows')
    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):

    locators = ButtonsPageLocators()

    @allure.step('click on different  buttons')
    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(
                self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)
        if type_click == "right":
            self.action_rigth_click(self.element_is_visible(
                self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)
        if type_click == "click":
            buttons_list = self.element_is_present(self.locators.BUTTON_LIST)
            left_click_button = buttons_list.find_element(
                "xpath", self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    @allure.step('check clicked button')
    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):

    locators = LinksPageLocators()

    @allure.step('check simple link')
    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    @allure.step('check broken link')
    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code


class UploadAndDownloadPage(BasePage):

    locators = UploadAndDownloadPageLocators()

    @allure.step('upload file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        # path = "C:\\fakepath\\" + file_name.split('/')[-1]
        # time.sleep(5)
        return file_name.split('\\')[-1], text.split('\\')[-1]

    @allure.step('download file')
    def download_file(self):
        link = self.element_is_present(
            self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'G:\\Python\\PycharmProjects\\selenium\\selenium_auto_qa_portfolio_project\\filetest{random.randint(0,999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            ofset = link_b.find(b'\\xxf\\xb8')
            f.write(link_b[ofset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file


class DynamicPropertiesPage(BasePage):

    locators = DynamicPropertiesPageLocators()

    @allure.step('check enable button')
    def check_enable_button(self):
        try:
            self.elements_is_clickable(
                self.locators.ENABLE_BUTTON).click()
        except TimeoutException:
            return False
        return True

    @allure.step('check changed of color')
    def check_changed_of_color(self):
        color_button = self.element_is_present(
            self.locators.COLLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    @allure.step('check appear of button')
    def check_appear_button(self):
        try:
            self.element_is_visible(
                self.locators.VISIBLE_AFTER_5_SECONDS_BUTTON)
        except TimeoutException:
            return False
        return True
