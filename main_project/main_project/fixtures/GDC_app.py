from time import sleep
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select
from fixtures.base_app import BaseApp


class Checkout(BaseApp):
    def __init__(self, base_url="https://goededoelen.testconcepten.nl/"):
        super().__init__(base_url)

    # http://development.nxte.nl/Cadeau_Concepten/PRCA1601-GoedeDoelen-Cadeaukaart
    # https://goededoelen.testconcepten.nl/
    # https://www.goededoelen-cadeaukaart.nl

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element_by_class_name("agree-button") .click()
        except Exception:
            pass

    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_css_selector("div > div > div > div > div > div:nth-child(3) > a").click()

    def close(self):
        sleep(2)
        self.driver.close()
