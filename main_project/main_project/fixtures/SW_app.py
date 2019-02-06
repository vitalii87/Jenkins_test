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
    def __init__(self, base_url="http://development.nxte.nl/Cadeau_Concepten/SAWE1501-Sauna-Wellness"):
        super().__init__(base_url)

    # http://development.nxte.nl/Cadeau_Concepten/SAWE1501-Sauna-Wellness
    # https://saunawellnesscadeaukaart.testconcepten.nl
    # https://www.saunawellnesscadeaukaart.nl

    def click_and_choose(self):
        driver = self.driver
        sleep(1)
        driver.find_element_by_css_selector(".green-button").click()
        driver.find_element_by_id("edit-giftcard-sell-price").clear()

    def close(self):
        sleep(2)
        self.driver.quit()
