import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.edit_player_form import EditPlayer
from pages.players_list import PlayersList
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddLanguageToExistingPlayerForm(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_remove_language_from_existing_player(self):
        TestLoginPage.test_login_to_the_system(self)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_players_button()
        players_list = PlayersList(self.driver)
        players_list.click_on_player()
        edit_player_page = EditPlayer(self.driver)
        edit_player_page.click_on_remove_language_button()
        edit_player_page.click_on_submit_button()
        self.driver.save_screenshot("../screenshots/TC-4.png")
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
