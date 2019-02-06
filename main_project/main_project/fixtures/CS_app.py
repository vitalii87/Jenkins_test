from selenium import webdriver
from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC


class CScheckout:
    def __init__(self, base_url="http://development.nxte.nl/Cadeau_Concepten/CACO1708-CadeauService/"):
        # https://cadeauservice.testconcepten.nl/
        # http://development.nxte.nl/Cadeau_Concepten/CACO1708-CadeauService/
        self.driver = webdriver.Chrome()
        self.base_url = base_url
        self.driver.get(base_url)
        self.driver.implicitly_wait(5)

    def alert_accept(self, message):
        driver = self.driver
        alert = driver.switch_to.alert
        assert message in alert.text
        alert.accept()

    def submit_status(self):
        driver = self.driver
        driver.find_element_by_xpath("//input[@value='Submit status']").click()

    def select_bank(self):
        driver = self.driver
        driver.find_element_by_id("brq_SERVICE_ideal_issuer").click()
        Select(driver.find_element_by_id("brq_SERVICE_ideal_issuer")).select_by_visible_text("ABNAMRO Bank")
        driver.find_element_by_xpath("//option[@value='ABNANL2A']").click()
        driver.find_element_by_id("button_continue").click()

    def redirection_to_boockaroo(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody[2]/tr[1]/td/select/optgroup/option[1]").click()
        sleep(1)

    def click_to_confirm(self):
        driver = self.driver
        sleep(1)
        # driver.find_element_by_class_name("iradio icheck-item icheck[itkn1] checked").click()
        driver.find_element_by_id("edit-submit").click()
        sleep(1)

    def to_one_adress(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='edit-send-buttons']/div/label").click()
        sleep(2)

    def fake_next_step(self):
        # next
        driver = self.driver
        driver.find_element_by_class_name("fake-next-step").click()

    def pers_message(self, text):
        driver = self.driver
        sleep(1)
        driver.find_element_by_id("edit-s-remark").send_keys(text)
        driver.find_element_by_id("submit-product10770").click()

    def choosing_to_first(self):
        # choosing to first card:
        driver = self.driver

        # driver.find_element_by_class_name("wrapper-for-giftcard-837").click()
        # driver.find_element_by_id("submit-product837").click()
        driver.find_element_by_class_name("wine-for-giftcard-8490").click()
        driver.find_element_by_id("submit-product8490").click()

    def next(self):
        # next
        driver = self.driver
        driver.find_element_by_id("edit-submit").click()
        sleep(1)

    def second_card(self, quantity, price):
        # second card card
        driver = self.driver
        driver.find_element_by_id("qty-card-field-690").clear()
        driver.find_element_by_id("qty-card-field-690").send_keys(quantity)
        driver.find_element_by_id("price-card-field-690").send_keys(price)
        driver.find_element_by_id("submit-card690").click()

    def first_card(self, quantity, price):
        # first card
        driver = self.driver
        driver.find_element_by_id("qty-card-field-249").clear()
        driver.find_element_by_id("qty-card-field-249").send_keys(quantity)
        driver.find_element_by_id("price-card-field-249").send_keys(price)
        driver.find_element_by_id("submit-card249").click()

    def click_on_order(self):
        driver = self.driver
        driver.find_element_by_css_selector('.menu-mlid-3848 > a:nth-child(1)').click()

    def login(self, user, passwd):
        # log-in
        driver = self.driver
        # driver.save_screenshot('one.png')
        driver.find_element_by_name('name').send_keys(user)
        driver.find_element_by_name('pass').send_keys(passwd)
        driver.find_element_by_id('edit-submit').click()

        # !reorder class!

    def click_on_reorder(self):
        driver = self.driver
        # driver.get("http://development.nxte.nl/Cadeau_Concepten/CACO1708-CadeauService")
        driver.find_element_by_css_selector(".menu-mlid-3849 > a:nth-child(1)").click()

    def addition_cards(self):
        driver = self.driver
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[5]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[5]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[5]").click()
        sleep(2)
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[4]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[4]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[4]").click()
        sleep(2)
        # func of 6 time clicking
        i = 0
        while i <= 5:
            driver.find_element_by_xpath("(//a[contains(text(),'+')])[6]").click()
            i += 1
        sleep(2)
        # go to next
        # driver.find_element_by_class_name("fake-next-step").click()
        # addition wrappers

    def addition_wrappers(self):
        driver = self.driver
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[2]").click()
        sleep(2)
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[3]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[3]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'+')])[3]").click()
        # testing_activation

    def click_on_activation(self):
        driver = self.driver
        driver.find_element_by_css_selector("#block-menu-block-3 > div > div > ul > li.first.leaf.menu-mlid-3846 > a").click()

    def setup_cards(self):
        driver = self.driver
        driver.find_element_by_id("edit-qty").click()
        driver.find_element_by_id("edit-qty").clear()
        driver.find_element_by_id("edit-qty").send_keys("3")
        driver.find_element_by_id("edit-amount").click()
        driver.find_element_by_id("edit-amount").clear()
        driver.find_element_by_id("edit-amount").send_keys("10")
        driver.find_element_by_xpath("//div[@id='personalized-cards-wrapper']/div/div/div/div").click()
        driver.find_element_by_id("edit-serial").click()
        driver.find_element_by_id("edit-serial").clear()
        driver.find_element_by_id("edit-serial").send_keys("6064000000000000000")
        driver.find_element_by_xpath("(//input[@name='serial'])[2]").click()
        driver.find_element_by_xpath("(//input[@name='serial'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='serial'])[2]").send_keys("6064000000000000001")
        driver.find_element_by_xpath("(//input[@name='serial'])[3]").click()
        driver.find_element_by_xpath("(//input[@name='serial'])[3]").clear()
        driver.find_element_by_xpath("(//input[@name='serial'])[3]").send_keys("6064000000000000002")
        driver.find_element_by_id("edit-submit").click()
        driver.find_element_by_id("edit-submit").click()
        sleep(2)

    def close(self):
        sleep(2)
        self.driver.quit()
