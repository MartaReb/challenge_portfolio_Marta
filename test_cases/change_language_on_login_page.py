import os
import unittest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        super(TestLoginPage, self).setUp(self)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.select_language("polski")
        user_login.page_in_polish_language()
        self.driver.save_screenshot("../screenshots/TC-2.1.png")
        user_login.select_language("english")
        user_login.page_in_english_language()
        self.driver.save_screenshot("../screenshots/TC-2.2.png")
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
