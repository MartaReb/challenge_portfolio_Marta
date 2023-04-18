from pages.base_page import BasePage


class AddMatchForm(BasePage):
    my_team_input_xpath = "//*[@name='myTeam']"
    enemy_team_input_xpath = "//*[@name='enemyTeam']"
    my_team_score_input_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_input_xpath = "//*[@name='enemyTeamScore']"
    date_input_xpath = "//*[@name='date']"
    match_at_home_radio_xpath = "//*[@name='matchAtHome'][@value='true']"
    match_out_home_radio_xpath = "//*[@name='matchAtHome'][@value='false']"
    tshirt_color_input_xpath = "//*[@name='tshirt']"
    league_input_xpath = "//*[@name='league']"
    time_played_input_xpath = "//*[@name='timePlayed']"
    player_number_input_xpath = "//*[@name='number']"
    web_match_input_xpath = "//*[@name='webMatch']"
    general_input_xpath = "//*[@name='general']"
    rating_input_xpath = "//*[@name='rating']"
    submit_button_xpath = "//*[span[text()='Submit']]"
    clear_button_xpath = "//*[span[text()='Clear']]"


pass
