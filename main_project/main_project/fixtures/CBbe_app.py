# from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains

from fixtures.base_app import BaseApp
from locators.locators import CheckoutLocators, CBbelocators


class Checkout(BaseApp):
    def __init__(self, base_url="https://cadeaubonbe.testconcepten.nl/"):
        super().__init__(base_url)
# https://cadeaubonbe.testconcepten.nl/
# http://development.nxte.nl/Cadeau_Concepten/CACO1802-Cadeaubon.be/
# https://www.cadeaubon.be/

    def click_on_keuze(self):
        driver = self.driver
        hov_first = driver.find_element_by_css_selector("#main-content .view-content .views-row-1 .ds-1col")
        sleep(1)
        click_add = driver.find_element_by_xpath(
            "//*[@id='block-views-card-types-block-1']/div/div/div[2]/div[1]/div/div[3]/div[2]/div/div/p/a")
        ActionChains(driver).move_to_element(hov_first).click(click_add).perform()
        sleep(1)

    def fill_form(self, name, surename, zip, house, phone, email, street, city):
        driver = self.driver
        driver.find_element(*CheckoutLocators.NAME).send_keys(name)
        driver.find_element(*CheckoutLocators.LASTNAME).send_keys(surename)
        driver.find_element(*CheckoutLocators.ZIPCODE).send_keys(zip)
        driver.find_element(*CheckoutLocators.HOUSE_NUMBER).send_keys(house)
        sleep(2)
        driver.find_element(*CheckoutLocators.PHONE).send_keys(phone)
        driver.find_element(*CBbelocators.STREET).send_keys(street)
        driver.find_element(*CBbelocators.CITY).send_keys(city)
        sleep(2)
        driver.find_element(*CheckoutLocators.EMAIL).send_keys(email)
        driver.find_element(*CheckoutLocators.NEXT_STEP2).click()

    def close(self):
        sleep(2)
        self.driver.close()
