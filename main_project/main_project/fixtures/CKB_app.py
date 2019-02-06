# from selenium import webdriver
from time import sleep
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select
from fixtures.base_app import BaseApp
# from page_obj_style.locators import CBLocators


class Checkout(BaseApp):
    def __init__(self, base_url="https://cadeaukaartbestellen.testconcepten.nl/"):
        super().__init__(base_url)
        # http://development.nxte.nl/Cadeau_Concepten/CACO1705-Cadeaukaart-bestellen/
        # https://cadeaukaartbestellen.testconcepten.nl/
        # https://www.cadeaukaartbestellen.nl/

    def click_on_keuze(self):
        driver = self.driver
        hov_first = driver.find_element_by_css_selector("#main-content .content .views-row-1 .ds-1col")
        sleep(1)
        click_add = driver.find_element_by_xpath(
            "//*[@id='block-views-card-types-block-1']/div/div/div[2]/div[1]/div/div[3]/div/div/p/a")
        ActionChains(driver).move_to_element(hov_first).click(click_add).perform()
        sleep(1)
        driver.find_element_by_css_selector("#block-system-main > div > div > div.group-header > div.field.field-name-card-shop-link.field-type-ds.field-label-hidden > div > div > p > a").click()
        sleep(1)

    def close(self):
        sleep(2)
        self.driver.close()
