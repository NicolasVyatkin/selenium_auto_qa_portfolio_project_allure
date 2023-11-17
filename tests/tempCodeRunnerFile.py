import time
from pages.alerts_frame_windows_page import AlertsPage, BrowserWindowsPage, IframePage, ModalDialogsPage, NestedFramesPage


class TestAlertsFrameWindow:

    class TestBrowserWindowsPage:
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(
                driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
