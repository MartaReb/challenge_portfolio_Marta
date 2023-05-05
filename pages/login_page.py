import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_url = "https://scouts-test.futbolkolektyw.pl/login"
    expected_title = "Scouts panel - sign in"
    header_login_form_xpath = "//*[text()='Scouts Panel']"
    expected_header = "Scouts Panel"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    expected_reminder_in_polish = "Przypomnij hasło"
    dropdown_language_list_xpath = "//*[contains(@class, 'MuiSelect-root')]"
    reminder_in_english_hyperlink_xpath = "//*[text()='Remind password']"
    expected_reminder_in_english = "Remind password"
    reminder_in_polish_hyperlink_xpath = "//*[text()='Przypomnij hasło']"
    english_language_xpath = "//*[@data-value='en']"
    polish_language_xpath = "//*[@data-value='pl']"
    invalid_message_xpath = "//*[text()='Identifier or password invalid.']"
    expected_invalid_header = "Identifier or password invalid."


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def header_of_login_form(self):
        self.assert_element_text(self.driver, self.header_login_form_xpath, self.expected_header)

    def check_invalid_message(self):
        self.assert_element_text(self.driver, self.invalid_message_xpath, self.expected_invalid_header)

    def select_language(self, language):
        self.click_on_the_element(self.dropdown_language_list_xpath)
        if language == "english":
            self.click_on_the_element(self.english_language_xpath)
        else:
            self.click_on_the_element(self.polish_language_xpath)

    def page_in_english_language(self):
        self.wait_for_visibility_of_element_located(self.reminder_in_english_hyperlink_xpath)
        self.assert_element_text(self.driver, self.reminder_in_english_hyperlink_xpath, self.expected_reminder_in_english)

    def page_in_polish_language(self):
        self.wait_for_visibility_of_element_located(self.reminder_in_polish_hyperlink_xpath)
        self.assert_element_text(self.driver, self.reminder_in_polish_hyperlink_xpath, self.expected_reminder_in_polish)
