from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def find_visible_element(self, locator):
        return self._wait.until(visibility_of_element_located(locator))

    def find_clicable_element(self, locator):
        return self._wait.until(element_to_be_clickable(locator))

    @property
    def current_url(self):
        return self.driver.current_url
