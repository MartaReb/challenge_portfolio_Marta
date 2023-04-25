import os
import time
import unittest
from selenium import webdriver

from pages.add_player_form import AddPlayerForm
from pages.dashboard import Dashboard
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestOpenAddPlayer(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_open_add_player(self):
        TestLoginPage.test_login_to_the_system(self)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_add_player_link()
        add_player_form = AddPlayerForm(self.driver)
        add_player_form.title_of_page()

        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
