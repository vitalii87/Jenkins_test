from time import sleep

from fixtures.base_app import BaseApp
from locators.locators import CheckoutLocators


class Checkout(BaseApp):
    def __init__(self, base_url="http://development.nxte.nl/Cadeau_Concepten/CACO1612-KKC-2.0/cadeaukaarten"):
        super().__init__(base_url)

    # http://development.nxte.nl/Cadeau_Concepten/CACO1612-KKC-2.0/cadeaukaarten
    # https://kerstkeuze.testconcepten.nl/cadeaukaarten
    # https://www.kerstkeuzecadeau.nl/cadeaukaarten

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element(*CheckoutLocators.ACCEPT_COOKIE_BUTTON).click()
        except Exception:
            pass

    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_css_selector(".field-item .even > a").click()
        driver.find_element_by_css_selector(".group-top-buttons-group a").click()

    def close(self):
        sleep(2)
        self.driver.close()
