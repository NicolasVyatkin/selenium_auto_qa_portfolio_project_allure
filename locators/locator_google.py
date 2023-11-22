from selenium.webdriver.common.by import By


# locators == selectors == element that need to be checked
# '#' - means id
# 'for=' - for sycle if radio neads to be tested


class FormPageLocators:
    """class that contains locators"""
    SEARCH_FIELD = (By.CSS_SELECTOR, '#APjFqb')
