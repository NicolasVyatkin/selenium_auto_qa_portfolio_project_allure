﻿from selenium.webdriver.common.by import By
import random


class AccordianPageLocators:

    CARD_HEADER = (By.CSS_SELECTOR,
                   f'div[id="section{random.randint(1,3)}Heading"]')

    SECTION_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    # multiple field
    TYPE_MULTIPLE_COLOR_NAMES_INPUT = (
        By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    TYPE_MULTIPLE_COLOR_NAMES_VALUE = (
        By.CSS_SELECTOR, 'div[class="css-12jo7m5 auto-complete__multi-value__label"]')
    TYPE_MULTIPLE_COLOR_NAMES_VALUE_REMOVE = (
        By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    # single field
    TYPE_SINGLE_COLOR_NAMES_INPUT = (
        By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    TYPE_SINGLE_COLOR_NAMES_VALUE = (
        By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerPageLocators:

    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (
        By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (
        By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (
        By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (
        By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (
        By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (
        By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = (
        By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (
        By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (
        By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class SliderPageLocators:

    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')
    SLIDER_POSITION_INPUT = (
        By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')


class ProgressBarPageLocators:

    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')


class TabsPageLocators:
    TAB_WHAT = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    TAB_ORIGIN = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    TAB_USE = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    TAB_MORE = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')

    TAB_WHAT_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    TAB_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    TAB_USE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    TAB_MORE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')


class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TOOL_TIP_BUTTON = (
        By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    TOOL_TIP_FIELD = (
        By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK = (By.XPATH, '//*[.="Contrary"]')
    TOOL_TIP_CONTRARY = (
        By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    SECTION_LINK = (By.XPATH, '//*[.="1.10.32"]')
    TOOL_TIP_SECTION = (
        By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuPageLocators:

    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')


class SelectMenuPageLocators:
    SELECT_VALUE = (By.CSS_SELECTOR, 'div[class=" css-1wa3eu0-placeholder"]')
    SELECT_VALUE_TEXT = (By.CSS_SELECTOR, 'div[class=" css-1uccc91-singleValue"]')
    
    SELECT_ONE = (By.CSS_SELECTOR, 'div[class=" css-1wa3eu0-placeholder"]')
    SELECT_ONE_TEXT = (By.CSS_SELECTOR, 'div[class=" css-1uccc91-singleValue"]')
    
    OLD_STULE_SELECT_MENU = (By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')
    
    
    MULT_SELECT_DROP_DOWN = (
        By.CSS_SELECTOR, 'div[class=" css-1wa3eu0-placeholder"]')
    SELECT_SELECT_DROP_DOWN_TEXT = (By.CSS_SELECTOR, 'div[class="css-12jo7m5"]')
    
    
    STANDART_MULTI_MENU = (By.CSS_SELECTOR, 'select[id="cars"]')
