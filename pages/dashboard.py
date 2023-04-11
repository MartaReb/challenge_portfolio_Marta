from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = "//div[div[span[text()='Main page']]]"
    players_button_xpath = "//div[div[span[text()='Players']]]"
    language_change_button_xpath = "//div[div[span[text()='Polski']]]"
    sign_out_button_xpath = "//div[div[span[text()='Sign out']]]"
    dev_team_contact_hyperlink_xpath = "//a[span[text()='Dev team contact']]"
    last_created_player_hyperlink_xpath = "//*[text()='Last created player']/following-sibling::a[1]"
    last_updated_player_hyperlink_xpath = "//*[text()='Last updated player']/following-sibling::a[1]"
    last_created_match_hyperlink_xpath = "//*[text()='Last created match']/following-sibling::a[1]"
    last_updated_match_hyperlink_xpath = "//*[text()='Last updated match']/following-sibling::a[1]"
    last_updated_report_hyperlink_xpath = "//*[text()='Last updated report']/following-sibling::a"
    add_player_hyperlink_xpath = "//a[@href='/en/players/add']"


pass
