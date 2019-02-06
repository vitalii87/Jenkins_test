from selenium import webdriver
from time import sleep
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from fixtures.base_app import BaseApp2

class Checkout(BaseApp2):
    def __init__(self, base_url="http://horecacadeaukaart.testconcepten.nl"):
        super().__init__(base_url)

    # http://development.nxte.nl/Cadeau_Concepten/CACO1602_NHC
    # http://horecacadeaukaart.testconcepten.nl
    # https://www.horecacadeaukaart.nl

    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_class_name("green-button").click()

    def close(self):
        sleep(2)
        self.driver.close()
