from pages.base_page import BasePage


class PlayersList(BasePage):
    player_name_on_the_list = "//*[@data-testid='MUIDataTableBodyRow-3']/td[1]"

    def click_on_player(self):
        self.wait_for_visibility_of_element_located(self.player_name_on_the_list)
        self.click_on_the_element(self.player_name_on_the_list)

