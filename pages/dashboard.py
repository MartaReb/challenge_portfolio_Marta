from pages.base_page import BasePage
import time

class Dashboard(BasePage):
    main_page_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    language_change_button_xpath = "//*[text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    dev_team_contact_hyperlink_xpath = "//*[span[text()='Dev team contact']]"
    last_created_player_hyperlink_xpath = "//div[3]/div/div/a[1]"
    name_of_last_created_player_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    expected_last_created_player = "WIOSNA LATO"
    last_updated_player_hyperlink_xpath = "//div[3]/div/div/a[2]"
    last_created_match_hyperlink_xpath = "//div[3]/div/div/a[3]"
    last_updated_match_hyperlink_xpath = "//div[3]/div/div/a[4]"
    last_updated_report_hyperlink_xpath = "//div[3]/div/div/a[5]"
    add_player_hyperlink_xpath = "//*[@href='/en/players/add']"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.main_page_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_add_player_link(self):
        self.wait_for_element_to_be_clickable(self.add_player_hyperlink_xpath)
        self.click_on_the_element(self.add_player_hyperlink_xpath)

    def click_on_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def click_on_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def last_created_player(self):
        self.wait_for_visibility_of_element_located(self.last_created_player_hyperlink_xpath)
        self.assert_element_text(self.driver, self.name_of_last_created_player_xpath, self.expected_last_created_player)
