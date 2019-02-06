from time import sleep

from fixtures.base_app import BaseApp
from locators.locators import KCCLocators


class Checkout(BaseApp):
    def __init__(self, base_url="https://www.kunstcultuurcadeaukaart.nl"):
        super().__init__(base_url)

    # http://development.nxte.nl/Cadeau_Concepten/CACO1601_KCC
    # https://kcc.testconcepten.nl
    # https://www.kunstcultuurcadeaukaart.nl

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element(*KCCLocators.ACCEPT_COOKIE_BUTTON_KCC).click()
        except Exception:
            pass

    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_class_name("green-button").click()

    def close(self):
        sleep(2)
        self.driver.close()
