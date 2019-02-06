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
    def __init__(self, base_url="http://development.nxte.nl/Cadeau_Concepten/CACO1710-Boeken.nl-d7"):
        super().__init__(base_url)

    # http://development.nxte.nl/Cadeau_Concepten/CACO1710-Boeken.nl-d7
    # https://boeken.testconcepten.nl
    # https://www.boeken.nl

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element_by_class_name("agree-button") .click()
        except Exception:
            pass

    def click_on_cadeau(self):
        driver = self.driver
        driver.find_element_by_xpath("(//a[contains(text(),'Cadeaukaart')])[3]").click()

    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_link_text("Direct bestellen").click()
        driver.find_element_by_xpath("//a[@id='edit-number--7-button']/span[2]").click()
        driver.find_element_by_id("ui-selectmenu-item-68").click()
        driver.find_element_by_xpath("//div[@id='edit-amount-form']/div[2]/span/label").click()
        driver.find_element_by_id("edit-amount").clear()
        driver.find_element_by_id("edit-amount").send_keys("10")
        driver.find_element_by_id("edit-next-button").click()
        driver.find_element_by_id("add-wrapper-to-cart-317").click()
        driver.find_element_by_link_text("Next").click()
        driver.find_element_by_xpath("//div[@id='edit-personal-data']/div/span/label").click()
        driver.find_element_by_xpath("//div[@id='edit-personal-data']/div[2]/span/label").click()
        driver.find_element_by_id("edit-mail").clear()
        driver.find_element_by_id("edit-mail").send_keys("vitalii+test-dev@nxte.nl")
        driver.find_element_by_xpath("//div[@id='edit-personal-data']/div[3]/span/label").click()
        driver.find_element_by_id("edit-phone-number").clear()
        driver.find_element_by_id("edit-phone-number").send_keys("101007")
        driver.find_element_by_xpath("//div[@id='edit-personal-data']/div[4]/span/label").click()
        driver.find_element_by_id("edit-first-name").clear()
        driver.find_element_by_id("edit-first-name").send_keys("First_name")
        driver.find_element_by_xpath("//div[@id='edit-personal-data']/div[5]/span/label").click()
        driver.find_element_by_id("edit-infix").clear()
        driver.find_element_by_id("edit-infix").send_keys("Ifix")
        driver.find_element_by_xpath("//div[@id='edit-address']/div/span/label").click()
        driver.find_element_by_id("edit-last-name").clear()
        driver.find_element_by_id("edit-last-name").send_keys("Last_name")
        driver.find_element_by_xpath("//div[@id='edit-address']/div[2]/span/label").click()
        driver.find_element_by_id("edit-postcode").clear()
        driver.find_element_by_id("edit-postcode").send_keys("1000AA")
        driver.find_element_by_xpath("//div[@id='edit-address']/div[3]/span/label").click()
        driver.find_element_by_id("edit-housenumber").clear()
        driver.find_element_by_id("edit-housenumber").send_keys("10")
        driver.find_element_by_id("edit-street").click()
        driver.find_element_by_id("edit-submit").click()
        driver.find_element_by_id("edit-submit").click()
        driver.find_element_by_xpath("//div[@id='edit-payment-method']/div/div").click()
        driver.find_element_by_id("edit-submit").click()

    def close(self):
        sleep(2)
        self.driver.close()
