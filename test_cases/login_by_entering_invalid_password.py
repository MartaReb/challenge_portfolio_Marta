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
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        super(TestLoginPage, self).setUp(self)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.header_of_login_form()
        user_login.type_in_email('user04@getnada.com')
        user_login.type_in_password('Test')
        user_login.click_on_sign_in_button()
        user_login.check_invalid_message()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()