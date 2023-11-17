import time
import allure
from pages.form_page import FormPage


@allure.suite('Forms')
class TestForm:

    @allure.feature('FormPage')
    class TestFormPage:

        @allure.title('Check form')
        def test_form_page(self, driver):
            """function that starts the test"""
            form_page = FormPage(
                driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            input_data = form_page.fill_form_fields()
            time.sleep(5)
            result = form_page.from_result()
            assert f'{input_data.first_name} {input_data.last_name}' == result[
                0], 'the form has not been filled'
            assert input_data.email == result[1], 'the form has not been filled'
            time.sleep(5)
