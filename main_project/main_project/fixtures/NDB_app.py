from time import sleep
from fixtures.base_app import BaseApp


class Checkout(BaseApp):
    def __init__(self, base_url="https://www.nationaledinerbon.nl"):
        super().__init__(base_url)
        # http://development.nxte.nl/Cadeau_Concepten/CACO1606-Nationale-Dinerbon
        # https://nationaledinerbon.testconcepten.nl
        # https://www.nationaledinerbon.nl

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonAcceptWrapper").click()
        except Exception:
            pass

    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_css_selector("#block-nodeblock-6482>div>div>div>div>div>div:nth-child(4)>a").click()
        sleep(2)

# --standard checkout--

    def close(self):
        sleep(2)
        self.driver.close()
