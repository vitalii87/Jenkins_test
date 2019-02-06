def check_lang(self):
    driver = self.driver
    # En = driver.find_element_by_css_selector("html[lang='en']")
    # Nl = driver.find_element_by_css_selector("html[lang='nl']")
    # view = driver.find_element_by_link_text("View our products")
    # view2 = driver.find_element_by_link_text("Bekijk ons assortiment")

    if driver.find_element_by_css_selector("html[lang='en']"):
        view = driver.find_element_by_link_text("View our products")
        assert view.text == "View our products"
        print("Lang is English")
    else:
        view2 = driver.find_element_by_link_text("Bekijk ons assortiment")
        assert view2.text == "Nederlands"
        print("lang is NL")
        # if Nl:
        #     assert view2.text == "Nederlands"
        #     print("Lang is Ned")
        # else:
        #     print("something wrong")