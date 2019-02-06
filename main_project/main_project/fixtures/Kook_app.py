
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
from page_obj_style.locators import CheckoutLocators


class Checkout(BaseApp):
    def __init__(self, base_url="http://development.nxte.nl/Cadeau_Concepten/CACO1701-KookCadeau"):
        super().__init__(base_url)

    # http://development.nxte.nl/Cadeau_Concepten/CACO1701-KookCadeau
    # https://kook-cadeau.testconcepten.nl
    # https://www.kook-cadeau.nl

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element(*CheckoutLocators.ACCEPT_COOKIE_BUTTON).click()
        except Exception:
            pass

    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_css_selector("#block-nodeblock-6482 > div > div > div > div > div > div:nth-child(3) > a").click()

    def close(self):
        sleep(2)
        self.driver.close()
