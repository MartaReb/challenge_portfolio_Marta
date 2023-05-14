import os
import time
import unittest
from selenium import webdriver

from pages.add_player_form import AddPlayerForm
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user04@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_add_player_link()
        add_player_form = AddPlayerForm(self.driver)
        add_player_form.type_in_name('Wiosna')
        add_player_form.type_in_surname('Lato')
        add_player_form.type_in_age('01/01/2000')
        add_player_form.type_in_main_position('bramkarz')
        add_player_form.click_on_submit_button()
        add_player_form.click_on_main_page_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.last_created_player()
        self.driver.save_screenshot("../screenshots/TC-3.png")
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
