from pages.base_page import BasePage
import time


class EditPlayer(BasePage):
    add_language_button_xpath = "//*[@aria-label='Add language']"
    languages_input_xpath = "//*[@name='languages[0]']"
    submit_button_xpath = "//*[@type='submit']"
    remove_language_button = "//div[15]/div[1]/button"

    def click_on_add_language(self):
        self.wait_for_visibility_of_element_located(self.add_language_button_xpath)
        self.click_on_the_element(self.add_language_button_xpath)

    def type_in_languages(self, language):
        self.field_send_keys(self.languages_input_xpath, language)

    def click_on_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_remove_language_button(self):
        self.wait_for_visibility_of_element_located(self.remove_language_button)
        self.click_on_the_element(self.remove_language_button)

    # def get_page_title(self, url):
    #     self.driver.get(url)
    #     return self.driver.title

pass
