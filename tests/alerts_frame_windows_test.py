import time
import allure
from pages.alerts_frame_windows_page import AlertsPage, BrowserWindowsPage, IframePage, ModalDialogsPage, NestedFramesPage


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindow:

    @allure.feature('Browser Windows')
    class TestBrowserWindowsPage:

        @allure.title('Checking the opening of a new tab')
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(
                driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "the new tab has not opened or an incorrect tab has opened"

        @allure.title('Checking the opening of a new window')
        def test_new_window(self, driver):
            """function that starts the test"""
            browser_windows_page = BrowserWindowsPage(
                driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_window()
            assert text_result == 'This is a sample page', "the new window has not opened or an incorrect tab has opened"

    @allure.feature('Alerts Page')
    class TestAlertsPage:
        @allure.title('Checking the opening of an alert')
        def test_alert(self, driver):
            alert_page = AlertsPage(
                driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', 'Button was not clicked?, or alert did not appeared'

        @allure.title('Checking the opening of the alert after 5 seconds')
        def test_alert_appear_after_5_sec(self, driver):
            alert_page = AlertsPage(
                driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'Button was not clicked, or alert did not appeared after 5 seconds'

        @allure.title('Checking the opening of the alert with confirm')
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(
                driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()

            assert alert_text == 'You selected Ok', 'Button was not clicked, or alert did not appeared'

        @allure.title('Checking the opening of the alert with prompt')
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert text in alert_text, "Alert did not show up"

    @allure.feature('Frame Page')
    class TestFramePage:
        @allure.title('Check the page with frames')
        def test_iframe(self, driver):
            frame_page = IframePage(
                driver, "https://demoqa.com/frames")
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page',
                                     '500px', '350px'], 'The frame does not exist'
            assert result_frame2 == ['This is a sample page',
                                     '100px', '100px'], 'The frame does not exist'

    @allure.feature('Nested Page')
    class TestNestedFramesPage:
        @allure.title('Check the page with nested frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(
                driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frames()
            assert parent_text == 'Parent frame', 'The nested frame does not exist'
            assert child_text == 'Child Iframe', 'The nested frame does not exist'

    @allure.feature('Modal Dialog Page')
    class TestModalDialogsPage:
        @allure.title('Check the page with modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialog_page = ModalDialogsPage(
                driver, "https://demoqa.com/modal-dialogs")
            modal_dialog_page.open()
            small, large = modal_dialog_page.check_modal_dialogs()
            assert small[1] < large[1], 'text from large dialog is less than text from small dialog'
            assert small[0] == 'Small Modal', 'The header is not "Small modal"'
            assert large[0] == 'Large Modal', 'The header is not "Large modal"'
