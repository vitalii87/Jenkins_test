from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from fixtures.base_app import BaseApp


class Checkout(BaseApp):
    def __init__(self, base_url="http://development.nxte.nl/Cadeau_Concepten/CACO1607-Cadeaubonnen/"):
        super().__init__(base_url)
        # arr = ()
        # # http://development.nxte.nl/Cadeau_Concepten/CACO1607-Cadeaubonnen/
        # # https://cadeaubon.testconcepten.nl/
        # # https://www.cadeaubon.nl/


    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonAcceptWrapper").click()
        except Exception:
            pass

    def click_on_keuze(self):
        driver = self.driver
        hov_first = driver.find_element_by_css_selector("#main-content .view-content .views-row-1 .ds-1col")
        sleep(1)
        click_add = driver.find_element_by_xpath(
            "//*[@id='block-views-card-types-block-1']/div/div/div[2]/div[1]/div/div[3]/div[2]/div/div/p/a")
        ActionChains(driver).move_to_element(hov_first).click(click_add).perform()
        sleep(1)

    def close(self):
        sleep(2)
        self.driver.close()
