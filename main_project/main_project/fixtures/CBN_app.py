from selenium import webdriver
from time import sleep
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from fixtures.base_app import BaseApp


class Checkout(BaseApp):
    def __init__(self, base_url="https://www.cadeaubonnen.nl/"):
        super().__init__(base_url)
        # https://cadeaubonnen2.testconcepten.nl/
        # http://development.nxte.nl/Cadeau_Concepten/CACO1613-CBN/
        # https://www.cadeaubonnen.nl/

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonAcceptWrapper").click()
        except Exception:
            pass

    def click_on_keuze(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        hov_first = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#block-views-card-types-block-1 > div > div > div.view-content > div.views-row.views-row-1.views-row-odd.views-row-first")))
        # #main-content .region .block .content .view .views-row .views-row-1
        # sleep(1)
        click_add = driver.find_element_by_xpath("//*[@id='block-views-card-types-block-1']/div/div/div[2]/div[1]/div/div[2]/div/div/p/a") # Keuze Cadeaukaart
        ActionChains(driver).move_to_element(hov_first).click(click_add).perform()
        sleep(1)
        driver.find_element_by_css_selector("#block-system-main > div > div > div.group-header > div.group-top-buttons-group.field-group-div > div.field.field-name-card-shop-link.field-type-ds.field-label-hidden > div > div > p > a").click()
        sleep(2)

    def close(self):
        sleep(2)
        self.driver.close()
