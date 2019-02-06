from selenium import webdriver
from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
from fixtures.base_app import BaseApp


class Checkout(BaseApp):
    def __init__(self, base_url="https://www.dinnercheque.nl"):
        super().__init__(base_url)
    # http://development.nxte.nl/Cadeau_Concepten/CACO1614-Dinnercheque
    # https://dinnercheque.testconcepten.nl
    # https://www.dinnercheque.nl
    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_class_name("button-green").click()

    def close(self):
        sleep(2)
        self.driver.close()


