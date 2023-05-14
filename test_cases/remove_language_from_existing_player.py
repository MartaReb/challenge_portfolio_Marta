import os
import time
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.edit_player_form import EditPlayer
from pages.login_page import LoginPage
from pages.players_list import PlayersList
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestRemoveLanguageFromExistingPlayerForm(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_remove_language_from_existing_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user04@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_players_button()
        players_list = PlayersList(self.driver)
        players_list.click_on_player()
        edit_player_page = EditPlayer(self.driver)
        edit_player_page.click_on_remove_language_button()
        edit_player_page.click_on_submit_button()
        self.driver.refresh()
        self.driver.save_screenshot("../screenshots/TC-6.png")
        edit_player_page.deleted_language_check()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
