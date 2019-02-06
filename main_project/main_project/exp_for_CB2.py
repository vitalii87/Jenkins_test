# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from locators.locators import CB2Locators


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element(*CB2Locators.ACCEPT_COOKIES).click()
            time.sleep(2)
        except Exception:
            print("--coocies policy absent--")

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://development.nxte.nl/Cadeau_Concepten/CACO1804-Cadeaubon.nl/nl")
        driver.find_element_by_css_selector(".header__logo > img:nth-child(1)").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
