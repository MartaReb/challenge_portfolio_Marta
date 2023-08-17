import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.dashboard import Dashboard
from pages.edit_player_form import EditPlayer
from pages.login_page import LoginPage
from pages.players_list import PlayersList
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddLanguageToExistingPlayerForm(unittest.TestCase):

    driver = None
    driver_service = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_language_to_existing_player_form(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user04@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_players_button()
        players_list = PlayersList(self.driver)
        players_list.click_on_player()
        edit_player_page = EditPlayer(self.driver)
        edit_player_page.click_on_add_language()
        edit_player_page.type_in_languages('polski')
        edit_player_page.click_on_submit_button()
        self.driver.refresh()
        self.driver.save_screenshot("../screenshots/TC-5.png")
        edit_player_page.add_language_check()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()