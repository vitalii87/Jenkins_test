from time import sleep

from fixtures.base_app import BaseApp


class Checkout(BaseApp):
    def __init__(self, base_url="https://nr1cadeau.testconcepten.nl"):
        super().__init__(base_url)

    # http://development.nxte.nl/Cadeau_Concepten/CACO1712-NR1-Cadeau/
    # https://nr1cadeau.testconcepten.nl
    # https://www.nr1cadeau.nl

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element_by_class_name("agree-button") .click()
        except Exception:
            pass

    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_css_selector("div > div > div > div > div > div:nth-child(3) > a").click()

    def close(self):
        sleep(2)
        self.driver.close()
