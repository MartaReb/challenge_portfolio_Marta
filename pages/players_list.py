import time

from pages.base_page import BasePage


class PlayersList(BasePage):
    player_name_on_the_list = "//*[@id='MUIDataTableBodyRow-3']/td[1]"

    def click_on_player(self):
        time.sleep(3)
        self.click_on_the_element(self.player_name_on_the_list)

