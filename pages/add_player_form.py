import time

from pages.base_page import BasePage


class AddPlayerForm(BasePage):
    expected_title = "Add player"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    age_field_xpath = "//*[@name='age']"
    main_position_field_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*[@type='submit']"
    clear_button_xpath = "//*[span[text()='Clear']]"
    main_page_button_xpath = "//*[text()='Main page']"
    expected_cleared_name_field = ""
    expected_cleared_surname_field = ""
    expected_cleared_age_field = ""
    expected_main_position_field = ""

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, position):
        self.field_send_keys(self.main_position_field_xpath, position)

    def click_on_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_clear_button(self):
        self.wait_for_element_to_be_clickable(self.clear_button_xpath)
        self.click_on_the_element(self.clear_button_xpath)

    def click_on_main_page_button(self):
        self.wait_for_element_to_be_clickable(self.main_page_button_xpath)
        self.click_on_the_element(self.main_page_button_xpath)

    def check_name_field_empty(self):
        self.wait_for_element_to_be_clickable(self.name_field_xpath)
        self.assert_element_value(self.driver, self.name_field_xpath, self.expected_cleared_name_field)

    def check_surname_field_empty(self):
        self.wait_for_element_to_be_clickable(self.name_field_xpath)
        self.assert_element_value(self.driver, self.name_field_xpath, self.expected_cleared_surname_field)

    def check_age_field_empty(self):
        self.wait_for_element_to_be_clickable(self.name_field_xpath)
        self.assert_element_value(self.driver, self.name_field_xpath, self.expected_cleared_age_field)

    def check_main_position_field_empty(self):
        self.wait_for_element_to_be_clickable(self.name_field_xpath)
        self.assert_element_value(self.driver, self.name_field_xpath, self.expected_main_position_field)