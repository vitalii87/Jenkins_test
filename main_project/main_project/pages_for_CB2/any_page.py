from selenium.webdriver.common.by import By

# from page_obj_style.locators import CB2Locators
from pages_for_CB2.base_page import Page


class AnyPage(Page):
    _LOGO = (By.CSS_SELECTOR, ".header__logo > img:nth-child(1)")

    @property
    def logo(self):
        return self.find_clicable_element(self._LOGO)



if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://development.nxte.nl/Cadeau_Concepten/CACO1804-Cadeaubon.nl")
    page = AnyPage(driver)
    page.logo.click()
    driver.quit()

