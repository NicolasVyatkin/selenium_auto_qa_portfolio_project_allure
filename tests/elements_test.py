import time
import random
import allure
from pages.elements_page import ButtonsPage, DynamicPropertiesPage, LinksPage, RadioButtonPage, TextBoxPage, CheckBoxPage, UploadAndDownloadPage, WebTablePage


@allure.suite("Elements")
class TestElements:
    @allure.feature('TextBox')
    class TestTextBox:

        @allure.title('Check TextBox')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_fielled_form()
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current address does not match"
            assert permanent_address == output_per_addr, "the permanent address does not match"

    @allure.feature('CheckBox')
    class TestCheckbox:

        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            """function that starts the test"""
            check_box_page = CheckBoxPage(
                driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "checkbokses have not been selected"

    @allure.feature('RadioButton')
    class TestRadioButton:

        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            """function that starts the test"""
            radio_button_page = RadioButtonPage(
                driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            # radio_button_page.click_on_the_radio_button('no')
            # output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            # assert output_no == 'No', "'No' have not been selected"

    @allure.feature('WebTable')
    class TestWebTable:

        @allure.title('Сheck to add a person to the table')
        def test_web_table_add_person(self, driver):
            """function that starts the test"""
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_added_person = web_table_page.add_new_person()
            result_table = web_table_page.check_new_added_person()
            assert new_added_person in result_table, 'added person was not found in the table'
            time.sleep(5)

        @allure.title('Check human search in table')
        def test_web_table_search_person(self, driver):
            """function that searches person in table"""
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, 'the person was not found by key word'

        @allure.title('Checking to update the persons info in the table')
        def test_webtable_update_person_info(self, driver):
            """function that chenges persons info in table"""
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person card has not been changed"

        @allure.title('Checking to remove a person from the table')
        def test_webtable_delete_person(self, driver):
            """function that deletes person from table"""
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found', "the person card has not been changed"

        @allure.title('Check the change in the number of rows in the table')
        def test_web_table_change_count_row(self, driver):
            """function that changes number of rows in table"""
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [
                5, 10, 20, 25, 50, 100], 'The number of rows in the table has not been changed or has been changed incorrectly'

    @allure.feature('Buttons page')
    class TestButtonsPage:

        @allure.title('Checking clicks of different types')
        def test_different_click_on_the_buttons(self, driver):
            """function that tests clicks on different buttons"""
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.click_on_different_button('double')
            right = buttons_page.click_on_different_button('right')
            click = buttons_page.click_on_different_button('click')
            assert double == "You have done a double click", "The double click button was not pressed"
            assert right == "You have done a right click", "The rigth click button was not pressed"
            assert click == "You have done a dynamic click", "The dynamic click button was not pressed"

    @allure.feature('Links page')
    class TestLinkPage:

        @allure.title('Checking the link')
        def test_check_link(self, driver):
            """function that tests clicks on work links"""
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "the link is broken or url is incorrect"

        @allure.title('Checking the broken link')
        def test_broken_link(self, driver):
            """function that tests clicks on broken links"""
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link(
                'https://demoqa.com/bad-request')
            assert response_code == 400, "The link works or the status code is not 400"

    @allure.feature('Upload and Download page')
    class TestUploadAndDownload:

        @allure.title('Check upload file')
        def test_upload_file(self, driver):
            """function that tests uploading files"""
            upload_download_page = UploadAndDownloadPage(
                driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, 'The file has not been uploaded'

        @allure.title('Check download file')
        def test_download_file(self, driver):
            """function that tests downloading files"""
            upload_download_page = UploadAndDownloadPage(
                driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True,  'The file has not been downloaded'

    @allure.feature('Dynamic properties page')
    class TestDynamicPropertiesPage:

        @allure.title('Check dynamic properties')
        def test_dynamic_propertie_color(self, driver):
            """function that tests dynamic buttons"""
            dynamic_properties_page = DynamicPropertiesPage(
                driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_after != color_before, 'colors have not been changed'

        @allure.title('Check appear button')
        def test_dynamic_properties_appearense(self, driver):
            """function that tests dynamic appearense of the buttons"""
            dynamic_properties_page = DynamicPropertiesPage(
                driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_button()
            assert appear is True, 'button did not apper after 5 seconds'

        @allure.title('Check enable button')
        def test_enable_button(self, driver):
            """function that tests dynamic appearense of the buttons"""
            dynamic_properties_page = DynamicPropertiesPage(
                driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable_button = dynamic_properties_page.check_enable_button()
            assert enable_button is True, 'button did not appear after 5 seconds'
