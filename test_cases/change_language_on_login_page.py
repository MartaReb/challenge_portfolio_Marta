import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

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
