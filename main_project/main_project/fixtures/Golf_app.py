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
import requests


class Checkout(BaseApp):
    def __init__(self, base_url="http://development.nxte.nl/Cadeau_Concepten/CACO1620-Golfbon/"):
        super().__init__(base_url)

    # http://development.nxte.nl/Cadeau_Concepten/CACO1620-Golfbon/
    # https://golfbon.testconcepten.nl
    # https://www.golfbon.nl

    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_class_name("button-green").click()

    def links(self):
        driver = self.driver
        print(driver.find_elements_by_tag_name("a"))

    def close(self):
        sleep(2)
        self.driver.close()
