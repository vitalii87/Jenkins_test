from time import sleep

from fixtures.base_app import BaseApp


class Checkout(BaseApp):
    def __init__(self, base_url="http://development.nxte.nl/Cadeau_Concepten/CACO1713-Cigo-DC/"):
        super().__init__(base_url)

    # http://development.nxte.nl/Cadeau_Concepten/CACO1713-Cigo-DC/
    # https://cigo.testconcepten.nl
    # https://cigo.diner-cadeau.nl

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element_by_class_name("agree-button") .click()
        except Exception:
            pass

    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_class_name("green-button").click()

    def close(self):
        sleep(2)
        self.driver.close()
