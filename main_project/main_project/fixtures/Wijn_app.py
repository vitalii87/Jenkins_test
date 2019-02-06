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
    def __init__(self, base_url="http://development.nxte.nl/Cadeau_Concepten/CACO1611-Wijn-Cadeaukaart"):
        super().__init__(base_url)
# http://development.nxte.nl/Cadeau_Concepten/CACO1611-Wijn-Cadeaukaart
# https://wijn.testconcepten.nl

    def click_and_choose(self):
        driver = self.driver
        sleep(1)
        driver.find_element_by_css_selector("#block-nodeblock-6482 > div > div > div > div > div > div:nth-child(3) > a").click()

    def close(self):
        sleep(2)
        self.driver.close()

