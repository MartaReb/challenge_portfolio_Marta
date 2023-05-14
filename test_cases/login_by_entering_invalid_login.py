import os
import unittest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginInByEnteringInvalidLogin(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system_by_entering_invalid_login(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user04@getnada.pl')
        user_login.type_in_password('Test-1234')
        user_login.click_on_sign_in_button()
        user_login.check_invalid_message()
        self.driver.save_screenshot("../screenshots/TC-8.png")
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
