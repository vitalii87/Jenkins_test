from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from .locators import CheckoutLocators


class BaseApp:
    def __init__(self, base_url=""):
        # capabilities = {
        #     "browserName": "chrome",
        #     "version": "67.0",
        #     "enableVNC": True,
        #     "enableVideo": True
        # }
        #
        # self.driver = webdriver.Remote(
        #     command_executor="http://selenoid:4444/wd/hub",
        #     desired_capabilities=capabilities)
        self.driver = webdriver.Chrome()
        self.base_url = base_url
        self.driver.get(base_url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
       # self.driver.set_window_size(375, 669)

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element(*CheckoutLocators.ACCEPT_COOKIE_BUTTON).click()
        except Exception:
            pass

    def first_step(self, quan):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(CheckoutLocators.SELECT_CARD))
        driver.find_element(*CheckoutLocators.SELECT_CARD).click()
        driver.find_element(*CheckoutLocators.CHOOSE_CARD_QUANTITY).click()
        # Select(driver.find_element_by_id("edit-giftcard-amount")).select_by_index("2")
        driver.find_element(*CheckoutLocators.CHOOSE_PRICE).send_keys(quan)
        sleep(1)
        driver.find_element(*CheckoutLocators.ADDITION_CARD).click()
        sleep(1)
        try:
            driver.find_element(*CheckoutLocators.ACCEPT_MESSAGE).click()
        except Exception:
            pass
        driver.find_element(*CheckoutLocators.NEXT_STEP2).click()

    def choose_v_pm_w(self, message):
        driver = self.driver
        try:
            wine_block = driver.find_element(*CheckoutLocators.VINE_BLOCK)
            hidden_button = driver.find_element(*CheckoutLocators.VINE_BUTTON)
            ActionChains(driver).move_to_element(wine_block).click(hidden_button).perform()
        except Exception:
            print("no vines")
        driver.find_element(*CheckoutLocators.MESSAGE).send_keys(message)
        driver.find_element(*CheckoutLocators.MESSAGE_BUTTON).click()
        sleep(1)
        try:
            wrapper = driver.find_element(*CheckoutLocators.WRAPPER_BLOCK)
            hidden_button2 = driver.find_element(*CheckoutLocators.WRAPPER_BUTTON)
            ActionChains(driver).move_to_element(wrapper).click(hidden_button2).perform()
        except Exception:
            print("no wrappers")
        sleep(1)
        driver.find_element(*CheckoutLocators.NEXT_STEP3).click()
        # driver.find_element(*CheckoutLocators.NEXT_STEP2).click()

    def fill_form(self, name, surename, zip, house, phone, email):
        driver = self.driver
        driver.find_element(*CheckoutLocators.NAME).send_keys(name)
        driver.find_element(*CheckoutLocators.LASTNAME).send_keys(surename)
        driver.find_element(*CheckoutLocators.ZIPCODE).send_keys(zip)
        driver.find_element(*CheckoutLocators.HOUSE_NUMBER).send_keys(house)
        driver.find_element(*CheckoutLocators.HOUSE_NUMBER2).click()
        sleep(3)
        driver.find_element(*CheckoutLocators.PHONE).send_keys(phone)
        sleep(1)
        driver.find_element(*CheckoutLocators.EMAIL).send_keys(email)
        sleep(1)
        driver.find_element(*CheckoutLocators.NEXT_STEP2).click()
        sleep(1)

    def choose_bank(self):
        driver = self.driver
        driver.find_element(*CheckoutLocators.IDEAL).click()
        driver.find_element(*CheckoutLocators.NEXT_STEP2).click()

    def last_step(self):
        driver = self.driver
        driver.find_element(*CheckoutLocators.LAST_STEP).click()

    def select_bank(self, bank):
        driver = self.driver
        driver.find_element(*CheckoutLocators.SELECT_BANK_IDEAL).click()
        Select(driver.find_element(*CheckoutLocators.SELECT_BANK_IDEAL)).select_by_visible_text(bank)
        driver.find_element(*CheckoutLocators.CONTINUE).click()

    def submit_status(self):
        driver = self.driver
        driver.find_element(*CheckoutLocators.SUBMIT).click()

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except:
            pass
        # TODO


class BaseApp2:
    def __init__(self, base_url=""):

        self.driver = webdriver.Chrome()
        self.base_url = base_url
        self.driver.get(base_url)
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def click_on_cookie(self):
        driver = self.driver
        try:
            driver.find_element_by_class_name("agree-button").click()
        except Exception:
            pass

    def click_and_choose(self):
        driver = self.driver
        sleep(1)
        driver.find_element_by_class_name("green-button").click()
        driver.find_element_by_id("edit-giftcard-sell-price").clear()

    def quan_cycle(self, fr, to):
        driver = self.driver
        for num in range(fr, to):
            try:
                driver.find_element_by_id("edit-giftcard-sell-price").send_keys(num)
                driver.find_element_by_id("giftcard-checkout-form").submit()
                sleep(1)
                driver.find_element_by_css_selector('.price+a').click()
                sleep(1)
            except Exception:
                print('\n'"no card with value - ", num)

    def click_on_card(self):
        driver = self.driver
        driver.find_element_by_class_name("green-button").click()

        driver.find_element_by_xpath("//*[@id='edit-giftcard-sell-price']").send_keys('10')
        driver.find_element_by_id("edit-giftcard-amount-button").send_keys('2')
        driver.find_element_by_id("edit-addcard").click()
        sleep(1)
        driver.find_element_by_css_selector(".form-item-giftcard-form-extra-include-message > div").click()
        # driver.find_element_by_xpath("//div[@id='edit-container-extra']/div/div").click()

        driver.find_element_by_id("edit-s-remark").send_keys("some message")
        driver.find_element_by_xpath("//div[@id='edit-giftcard-form-extra-product']/div/div").click()
        driver.find_element_by_id("6300").click()
        sleep(1)
        # driver.find_element_by_xpath("//div[@id='edit-giftcard-wrapper']/div/div").click()
        driver.find_element_by_id("7707").click()
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
        # Select(driver.find_element_by_id("brq_SERVICE_ideal_issuer")).select_by_visible_text("ABNAMRO Bank")
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
