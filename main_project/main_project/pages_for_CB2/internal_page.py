from selenium.webdriver.common.by import By

from pages_for_CB2.base_page import Page


class InternalPage(Page):
    MAIN_PAGE_LINK = (By.LINK_TEXT, "m")

    @property
    def sing_in_link(self):
        return self.find_clicable_element(self.MAIN_PAGE_LINK)

    def is_this_page(self):
        pass
