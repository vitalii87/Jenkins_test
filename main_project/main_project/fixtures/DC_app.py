from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC


class Checkout:
    def __init__(self, base_url="https://diner-cadeau.testconcepten.nl"):

        # http://development.nxte.nl/Cadeau_Concepten/PRCA1501-Diner-Cadeau
        # https://diner-cadeau.testconcepten.nl

        self.driver = webdriver.Chrome()
        self.base_url = base_url
        self.driver.get(base_url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        # self.driver.set_window_size(1366, 900)

    def click_and_choose(self):
        driver = self.driver
        driver.find_element_by_class_name("green-button").click()
        driver.find_element_by_id("edit-giftcard-sell-price").send_keys('10')
        driver.find_element_by_id("edit-giftcard-amount-button").send_keys('2')
        sleep(1)
        driver.find_element_by_id("edit-addcard").click()
        sleep(1)
        driver.find_element_by_xpath("//div[@id='edit-container-extra']/div/div").click()
        driver.find_element_by_id("edit-s-remark").send_keys("some message")
        driver.find_element_by_xpath("//div[@id='edit-giftcard-form-extra-product']/div/div").click()
        driver.find_element_by_id("6300").click()
        sleep(1)
        driver.find_element_by_xpath("//div[@id='edit-giftcard-wrapper']/div/div").click()
        driver.find_element_by_id("7707").click()


    def filling_form(self):
        driver = self.driver
        driver.find_element_by_id("edit-b-initials").clear()
        driver.find_element_by_id("edit-b-initials").send_keys("Vit")
        driver.find_element_by_id("edit-b-lastname").clear()
        driver.find_element_by_id("edit-b-lastname").send_keys("Test")
        driver.find_element_by_id("edit-b-address").clear()
        driver.find_element_by_id("edit-b-address").send_keys("some_street")
        driver.find_element_by_id("edit-b-housenr").clear()
        driver.find_element_by_id("edit-b-housenr").send_keys("10")
        driver.find_element_by_xpath("//div[@id='edit-address-row-2']/div/span/label").click()
        driver.find_element_by_xpath("//div[@id='edit-address-row-2']/div/span/label").click()
        driver.find_element_by_xpath("//div[@id='edit-address-row-2']/div[2]/span/label").click()
        driver.find_element_by_id("edit-b-zipcode").clear()
        driver.find_element_by_id("edit-b-zipcode").send_keys("1000AA")
        driver.find_element_by_xpath("//div[@id='edit-left']/div[13]/span/label").click()
        driver.find_element_by_id("edit-b-city").clear()
        driver.find_element_by_id("edit-b-city").send_keys("Some_city")
        driver.find_element_by_xpath("//div[@id='edit-left']/div[15]/span/label").click()
        driver.find_element_by_id("edit-b-phone").clear()
        driver.find_element_by_id("edit-b-phone").send_keys("phone")
        driver.find_element_by_id("edit-b-email").clear()
        driver.find_element_by_id("edit-b-email").send_keys("vitalii+test@nxte.nl")
        driver.find_element_by_xpath("//div[@id='edit-payment']/div[3]/div").click()
        driver.find_element_by_id("edit-submit").click()

    def select_bank(self):
        driver = self.driver
        driver.find_element_by_id("brq_SERVICE_ideal_issuer").click()
        Select(driver.find_element_by_id("brq_SERVICE_ideal_issuer")).select_by_visible_text("ABNAMRO Bank")
        driver.find_element_by_xpath("//option[@value='ABNANL2A']").click()
        driver.find_element_by_id("button_continue").click()

    def submit_status(self):
        driver = self.driver
        driver.find_element_by_xpath("//input[@value='Submit status']").click()

    def alert_accept(self):
        driver = self.driver
        alert = driver.switch_to.alert
        # assert message in alert.text
        alert.accept()

    def close(self):
        sleep(2)
        self.driver.close()

