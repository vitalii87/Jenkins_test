from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from main_project.test_for_CB2.base_app import BaseApp
from main_project.test_for_CB2.locators import CB2Locators, CheckoutLocators
from selenium.webdriver.support.ui import WebDriverWait


class Checkout(BaseApp):

    def click_on_cookie(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        try:
            ec = wait.until(EC.element_to_be_clickable(CB2Locators.ACCEPT_COOKIES))
            ec.click()
        except NoSuchElementException:
            print("--coocies policy absent--")

    def check_existing_of_elements(self):
        driver = self.driver
        saldo = driver.find_element_by_link_text("Saldo check")
        try:
            driver.find_element_by_link_text("Saldo check")
        except Exception:
            print("no such element")
            # with pytest.raises(Exception):
            assert "Saldo check" in saldo.text
            # except Exception:
            #     print("wrong word")

    def check_lang(self):
        driver = self.driver
        try:
            driver.find_element(*CB2Locators.MAIN_LANG)
            view = driver.find_element(*CB2Locators.VIEW_OUR_PRODUCTS)
            assert view.text == "View all categories"
            print("\n *Lang is English*")
        except Exception:
            print("\n *Lang is NL*")
            view2 = driver.find_element(*CB2Locators.VIEW_OUR_PRODUCTS_NL)
            assert view2.text == "Bekijk ons assortiment"
        sleep(3)
            # TESTING SEARCH
            #  @pytest.mark.parametrize('key')

    def click_and_tape(self, words):
        driver = self.driver
        for key in words:
            driver.find_element(*CB2Locators.INPUT_FIELD_UP).click()
            driver.find_element(*CB2Locators.INPUT_FIELD_UP2).send_keys(key)
            sleep(1)
            driver.find_element(*CB2Locators.INPUT_FIELD_SUBMIT).click()
            sleep(2)
            driver.find_element(*CB2Locators.HOME_LOGO).click()

    def check_suggestions(self, word):
        driver = self.driver
        driver.find_element(*CB2Locators.INPUT_FIELD).click()
        driver.find_element(*CB2Locators.INPUT_FIELD_2).send_keys(word)
        sleep(2)
        a = driver.find_element(*CB2Locators.SEARCH_SUGGESTIONS)
        # print(a.text)
        assert "nike cadeaukaart" in a.text

    # TEST HEADER
    def check_logo(self):
        try:
            driver = self.driver
            alt = "Home"
            logo = driver.find_element(*CB2Locators.HOME_LOGO)
            print('\n+logo is fine+')
            # assert alt in logo
        except Exception:
            print("\n --something wrong with logo--")

    def check_up_hower(self):
        try:
            driver = self.driver
            saldo = driver.find_element(*CB2Locators.SALDO_UP)
            saldo_before = (driver.find_element(*CB2Locators.SALDO_UP).value_of_css_property("color"))
            print("\n", saldo_before)
            color_1 = ('rgba(36, 21, 115, 1)') or ('rgb(36, 21, 115)')
            assert saldo_before in color_1
            # redeem = driver.find_element(*CB2Locators.REDEEM_UP)
            # upgrade = driver.find_element(*CB2Locators.UPGRADE_UP)
            # business = driver.find_element(*CB2Locators.BUSINESS_UP)
            hover = ActionChains(driver).move_to_element(saldo)
            hover.perform()
            sleep(2)
            color_2 = ('rgba(255, 77, 101, 1)')
            saldo_back = (driver.find_element(*CB2Locators.SALDO_UP).value_of_css_property("background-color"))
            print(saldo_back)
            print("+hover working+")
            assert saldo_back in color_2
        except Exception:
            print("--hover not working--")

            # ----------------------------
            # ---------CHECKOUT-----------
            # ----------------------------

    def choose_card(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.find_element(*CB2Locators.CHOOSE_SUGGESTED_CARD).click()
        # el = wait.until(EC.element_to_be_clickable(CB2Locators.CHOOSE_SUGGESTED_CARD))
        # el.click()
        sleep(5)

    def click_on_order(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        el = wait.until(EC.element_to_be_clickable(CB2Locators.CLICK_ON_ORDER))
        el.click()
        sleep(3)

    def choose_price_quan(self, quan):
        driver = self.driver
        driver.find_element(*CB2Locators.CLICK_ON_SUGPRICE).click()
        sleep(1)
        driver.find_element(*CB2Locators.CLICK_ON_QUAN).click()
        driver.find_element_by_css_selector("#edit-quantity-input-menu > li:nth-child(%s) > a" % quan).click()

    def click_op(self):
        driver = self.driver
        driver.find_element(*CB2Locators.CLICK_OP).click()
        sleep(3)

    def choose_wrapper(self):
        driver = self.driver
        driver.find_element(*CB2Locators.CHOOSE_WRAPPER).click()
        sleep(2)

    def choose_wine(self, q):
        driver = self.driver
        driver.find_element(*CB2Locators.CHOOSE_WINE).click()
        for i in range(q):
            driver.find_element(*CB2Locators.CLICK_ON_WINE).click()
        sleep(2)

    def choose_message(self, message):
        driver = self.driver
        driver.find_element(*CB2Locators.CLICK_ON_MESSAGE).click()
        driver.find_element(*CB2Locators.MESSAGE).send_keys(message)
        driver.find_element(*CB2Locators.ACCEPT_MESSAGE).click()
        sleep(1)

    def step_after_po(self):
        driver = self.driver
        driver.find_element(*CB2Locators.STEP_NEXT_AFTER_PO).click()
        sleep(3)

    def asserts(self, message):
        driver = self.driver
        driver.find_element(*CB2Locators.FIND_PERS_MESSAGE).click()
        mes = driver.find_element(*CB2Locators.FIND_PERS_MESSAGE_SHOWN)
        text = message
        try:
            assert text in mes.text
        except Exception:
            print("\n--problem with message--")

    def checkout_first(self):
        driver = self.driver
        driver.find_element(*CB2Locators.CHECKOUT_FIRST).click()

    def fill_form_checkout(self, name, prefix, last_name, email, phone, sh_nme,
                           sh_prefix, sh_lname, postcode, housenum, suffix):
        driver = self.driver
        driver.find_element(*CB2Locators.FILL_NAME).click()
        driver.find_element(*CB2Locators.FILL_NAME).send_keys(name)
        sleep(1)
        driver.find_element(*CB2Locators.FILL_PREFIX).send_keys(prefix)
        sleep(1)
        driver.find_element(*CB2Locators.FILL_LNAME).send_keys(last_name)
        driver.find_element(*CB2Locators.FILL_EMAIL).send_keys(email)
        driver.find_element(*CB2Locators.FILL_PHONE).send_keys(phone)
        driver.find_element(*CB2Locators.FILL_SHIPPING_NAME).send_keys(sh_nme)
        driver.find_element(*CB2Locators.FILL_SHIPPING_PREFIX).send_keys(sh_prefix)
        driver.find_element(*CB2Locators.FILL_SHIPPING_LNAME).send_keys(sh_lname)
        driver.find_element(*CB2Locators.EDIT_POSTCODE).send_keys(postcode)
        sleep(1)
        driver.find_element(*CB2Locators.EDIT_HOUSENUMBER).send_keys(housenum)
        driver.find_element(*CB2Locators.EDIT_SUFFIX).send_keys(suffix)

    def choose_deldate(self):
        driver = self.driver
        driver.find_element(*CB2Locators.CHOOSE_DELDATE).click()

    def choose_payment(self):
        driver = self.driver
        driver.find_element(*CB2Locators.CHOOSE_PAYMETH).click()

    def submit(self):
        driver = self.driver
        try:
            driver.find_element(*CB2Locators.SUBMIT).click()
            sleep(1)
        except Exception:
            print("--validation is not passed--")

    def select(self):
        driver = self.driver
        driver.find_element(*CheckoutLocators.SELECT_BANK_IDEAL).click()
        driver.find_element_by_xpath("//option[@value='ABNANL2A']").click()
        driver.find_element(*CheckoutLocators.CONTINUE).click()

    # ----------------------------
    # ------END OF CHECKOUT-------
    # ----------------------------

    # ----------------------------
    # ------REDEEM CHECKOUT-------
    # -----------START------------

    def click_on_redeem(self):
        driver = self.driver
        driver.find_element(*CB2Locators.CLICK_ON_REDEEM).click()

    def edit_cardnumber(self):
        driver = self.driver
        driver.find_element(*CB2Locators.EDIT_CARDNUMBER).send_keys("6064363043023118798")

    def submit_card(self):
        driver = self.driver
        driver.find_element(*CB2Locators.SUBMIT_CARD).click()

    def check_all_cards(self):
        driver = self.driver
        try:
            driver.find_element(*CB2Locators.ALL_CARDS).click()
            print("--Captcha doesn't working--")
        except Exception:
            print("++Captcha working++")


            # ----------------------------
            # ------REDEEM CHECKOUT-------
            # ------------END-------------




            # ------TEST_E-VOUCHERS--------

    def click_on_evoucher(self):
        driver = self.driver

    def check_dropdown_menu(self):
        driver = self.driver
        driver.find_element(*CB2Locators.DROPDOWN_MENU).click()
        sleep(1)

        l = [driver.find_element(*CB2Locators.DDM_ITEM1), driver.find_element(*CB2Locators.DDM_ITEM2),
             driver.find_element(*CB2Locators.DDM_ITEM3), driver.find_element(*CB2Locators.DDM_ITEM4)]
        for i in l:
            return i

        sleep(2)

    def close(self):
        self.driver.close()
