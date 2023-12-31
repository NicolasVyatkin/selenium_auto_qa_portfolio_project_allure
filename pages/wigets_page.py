﻿import time
import random
import allure
from generator.generator import generated_color, generated_date
from locators.wigets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, MenuPageLocators, ProgressBarPageLocators, SelectMenuPageLocators, SliderPageLocators, TabsPageLocators, ToolTipsPageLocators
from selenium.common.exceptions import TimeoutException

from selenium.webdriver import Keys


from pages.base_page import BasePage


class AccordianPage(BasePage):

    locators = AccordianPageLocators()

    @allure.step('check accordian widget')
    def check_accordian(self, accordian_num):
        accordian = {'first':
                     {'title': self.locators.SECTION_FIRST,
                      'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD},
                     }

        section_title = self.element_is_visible(
            accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(
                accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(
                accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):

    locators = AutoCompletePageLocators()

    @allure.step('fill multi autocomplete input')
    def check_fill_input_multi(self):
        colors = random.sample(
            next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.elements_is_clickable(
                self.locators.TYPE_MULTIPLE_COLOR_NAMES_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.RETURN)
        return colors

    @allure.step('remove value from multi autocomplete')
    def check_remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(
            self.locators.TYPE_MULTIPLE_COLOR_NAMES_VALUE))
        remove_button_list = self.elements_are_visible(
            self.locators.TYPE_MULTIPLE_COLOR_NAMES_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(
            self.locators.TYPE_MULTIPLE_COLOR_NAMES_VALUE))
        return count_value_before, count_value_after

    @allure.step('check colors in multi autocomplete')
    def check_color_in_multi(self):
        color_list = self.elements_are_present(
            self.locators.TYPE_MULTIPLE_COLOR_NAMES_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step('fill single autocomplete input')
    def check_fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(
            self.locators.TYPE_SINGLE_COLOR_NAMES_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    @allure.step('check color in single autocomplete')
    def check_color_in_single(self):
        color = self.element_is_visible(
            self.locators.TYPE_SINGLE_COLOR_NAMES_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step('change date')
    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(
            self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('change select date and time')
    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(
            self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(
            self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(
            self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(
            self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(
            self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):

    locators = SliderPageLocators()

    @allure.step('change slider value')
    def check_change_slider_value(self):
        value_before = self.element_is_visible(
            self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(
            self.locators.SLIDER_POSITION_INPUT)
        self.action_drag_and_drop_by_offset(
            slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(
            self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):

    locators = ProgressBarPageLocators()

    @allure.step('change progress bar value')
    def check_change_progress_bar(self):
        value_before = self.element_is_present(
            self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(
            self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 4))
        progress_bar_button.click()
        value_after = self.element_is_present(
            self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):

    locators = TabsPageLocators()

    @allure.step('check tabs')
    def check_tabs(self, name_tab):
        # what_button = self.element_is_visible(self.locators.TAB_WHAT)
        # origin_button = self.element_is_visible(self.locators.TAB_ORIGIN)
        # use_button = self.element_is_visible(self.locators.TAB_USE)
        # more_button = self.element_is_visible(self.locators.TAB_MORE)
        # what_button.click()
        # what_content = self.element_is_visible(
        #     self.locators.TAB_WHAT_CONTENT).text
        # origin_button.click()
        # origin_content = self.element_is_visible(
        #     self.locators.TAB_ORIGIN_CONTENT).text
        # use_button.click()
        # use_content = self.element_is_visible(
        #     self.locators.TAB_USE_CONTENT).text
        # more_button.click()
        # more_content = self.element_is_visible(
        #     self.locators.TAB_MORE_CONTENT).text

        tabs = {'what':
                {'title': self.locators.TAB_WHAT,
                 'content': self.locators.TAB_WHAT_CONTENT},
                'origin':
                    {'title': self.locators.TAB_ORIGIN,
                     'content': self.locators.TAB_ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.TAB_USE,
                     'content': self.locators.TAB_USE_CONTENT},
                'more':
                    {'title': self.locators.TAB_MORE,
                     'content': self.locators.TAB_MORE_CONTENT},
                }

        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        what_content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(what_content)


class ToolTipsPage(BasePage):

    locators = ToolTipsPageLocators()

    @allure.step('get text from tool tip')
    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    @allure.step('check tool tip')
    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(
            self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(
            self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK,
                                                              self.locators.TOOL_TIP_CONTRARY)
        tool_tip_text_section = self.get_text_from_tool_tips(
            self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section


class MenuPage(BasePage):

    locators = MenuPageLocators()

    @allure.step('check menu item')
    def check_menu(self):
        menu_item_list = self.elements_are_present(
            self.locators.MENU_ITEM_LIST)

        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            # self.element_is_visible(item)
            data.append(item.text)
        return data


class SelectMenuPage(BasePage):

    locators = SelectMenuPageLocators()

    @allure.step('check select value')
    def check_select_value(self):
        select_value = self.element_is_visible(self.locators.SELECT_VALUE)
        select_value.click()
        select_value.send_keys(Keys.RETURN)
        text= self.element_is_visible(self.locators.SELECT_VALUE_TEXT).text
        return text
        

    @allure.step('check select one')
    def check_one_select_value(self):
        select_value = self.element_is_visible(self.locators.SELECT_ONE)
        select_value.click()
        select_value.send_keys(Keys.RETURN)
        text= self.element_is_visible(self.locators.SELECT_ONE_TEXT).text
        return text
    @allure.step('check old style select menu')
    def check_old_style_select_menu(self):
        select_value = self.element_is_visible(self.locators.OLD_STULE_SELECT_MENU)
        select_value.click()
        select_value.send_keys(Keys.RETURN)
        text= self.element_is_visible(self.locators.OLD_STULE_SELECT_MENU).text
        return text

    @allure.step('check multi select drop group')
    def check_mult_select_drop_down(self):
        select_value = self.element_is_visible(self.locators.MULT_SELECT_DROP_DOWN)
        select_value.click()
        select_value.send_keys(Keys.RETURN)
        text= self.element_is_visible(self.locators.SELECT_SELECT_DROP_DOWN_TEXT).text
        return text

    @allure.step('check standart multi select')
    def check_standart_multi_select(self):
        select_value = self.element_is_visible(self.locators.STANDART_MULTI_MENU)
        select_value.click()
        #select_value.send_keys(Keys.RETURN)
        text= self.element_is_visible(self.locators.STANDART_MULTI_MENU).text
        return text
