from selenium.webdriver.common.by import By


class CBLocators:
    ACCEPT_COOKIE_BUTTON_CB = (By.XPATH, "//*[@id='CybotCookiebotDialogBodyLevelButtonAccept']")


class KCCLocators:
    ACCEPT_COOKIE_BUTTON_KCC = (By.ID, "CybotCookiebotDialogBodyLevelButtonAccept")


class CBbelocators:
    STREET = (By.ID, "edit-b-address")
    CITY = (By.ID, "edit-b-city")


# First priority
class CB2Locators:
    HOME_LOGO = (By.CSS_SELECTOR, ".header__logo")
    ACCEPT_COOKIES = (By.CLASS_NAME, "agree-button")
    MAIN_LANG = (By.CSS_SELECTOR, "html[lang='en']")
    VIEW_OUR_PRODUCTS = (By.ID, "block-menu-block-1")
    VIEW_OUR_PRODUCTS_NL = (By.ID, "block-menu-block-1")
    # UpSearch >
    INPUT_FIELD_UP = (By.CSS_SELECTOR, "span.sticky-placeholder-wrapper:nth-child(1)")
    INPUT_FIELD_UP2 = (By.ID, "edit-search-block-form--2")
    # Search >
    INPUT_FIELD = (By.CSS_SELECTOR, "span.sticky-placeholder-wrapper:nth-child(1) > label:nth-child(2)")
    INPUT_FIELD_2 = (By.ID, "edit-search")
    INPUT_FIELD_SUBMIT = (By.ID, "edit-submit")
    INPUT_FIELD_SUBMIT2 = (By.XPATH, "//*[@id='edit-submit']")
    SALDO_UP = (By.XPATH, "/html/body/header/div[1]/div/div/div[2]/div/div/ul/li[1]/a")
    REDEEM_UP = (By.XPATH, "/html/body/header/div[1]/div/div/div[2]/div/div/ul/li[2]/a")
    UPGRADE_UP = (By.CSS_SELECTOR, "/html/body/header/div[1]/div/div/div[2]/div/div/ul/li[3]/a")
    BUSINESS_UP = (By.CSS_SELECTOR, "/html/body/header/div[1]/div/div/div[2]/div/div/ul/li[4]/a")
    DROPDOWN_MENU = (By.CSS_SELECTOR, ".main-menu__toggle")
    DDM_ITEM1 = (By.CSS_SELECTOR, ".submenu__link")
    DDM_ITEM2 = (By.CSS_SELECTOR, ".menu-mlid-4021 > a:nth-child(1)")
    DDM_ITEM3 = (By.CSS_SELECTOR, ".menu-mlid-4022 > a:nth-child(1)")
    DDM_ITEM4 = (By.CSS_SELECTOR, ".menu-mlid-4023 > a:nth-child(1)")
    BUTTON_SEARCH_RES = (By.CSS_SELECTOR, ".button--default")
    SEARCH_SUGGESTIONS = (By.CSS_SELECTOR, "#main-search-form > div.suggestion-template")
    # CHECKOUT_LOCATORS >
    CHOOSE_SUGGESTED_CARD = (By.XPATH, "/html/body/div[2]/div[2]/div/section/div/div[3]/div/div/div/div/div/div[1]/div/div[1]/div/div/a")
    CLICK_ON_ORDER = (By.CSS_SELECTOR, ".form-type-radio")
    CLICK_ON_SUGPRICE = (By.CSS_SELECTOR, "#edit-popular-prices> div:nth-child(4) > label")
    CLICK_ON_QUAN = (By.CSS_SELECTOR, "#edit-quantity-input-button > span.ui-selectmenu-status")
# --CHOOSE_QUAN = (By.CSS_SELECTOR, "#edit-quantity-input-menu > li:nth-child(%s) > a")
    CHOOSE_WRAPPER = (By.CSS_SELECTOR, "#edit-wrappers-selection > div:nth-child(2) > label > div > div")
    CHOOSE_WINE = (By.CSS_SELECTOR, "#edit-tabs-radios-selection > div:nth-child(2) > label")
    CLICK_OP = (By.CSS_SELECTOR, "#edit-submit--3")
    CLICK_ON_WINE = (By.CSS_SELECTOR, "div.form-type-checkbox:nth-child(2) > label:nth-child(2) > div:nth-child(1) > div:nth-child(4) > span:nth-child(3)")
    CLICK_ON_MESSAGE = (By.CSS_SELECTOR, "div.form-item-tabs-radios-selection:nth-child(3)")
    MESSAGE = (By.ID, "edit-personal-message-input")
    ACCEPT_MESSAGE = (By.ID, "edit-button--3")
    STEP_NEXT_AFTER_PO = (By.CSS_SELECTOR, "a.ctools-close-modal:nth-child(3)")
    FIND_PERS_MESSAGE = (By.CSS_SELECTOR, ".cart-sidebar-wrapper .cart-body > div:first-child .personal-message-title")
    FIND_PERS_MESSAGE_SHOWN = (By.CSS_SELECTOR, ".cart-sidebar-wrapper .cart-body > div:first-child .personal-message-text")
    CHECKOUT_FIRST = (By.CSS_SELECTOR, ".order-step")
    FILL_NAME = (By.ID, "edit-b-firstname")
    FILL_PREFIX = (By.ID, "edit-b-prefix")
    FILL_LNAME = (By.ID, "edit-b-lastname")
    FILL_EMAIL = (By.ID, "edit-b-email")
    FILL_PHONE = (By.ID, "edit-b-phone")
    FILL_SHIPPING_NAME = (By.ID, "edit-s-firstname")
    FILL_SHIPPING_PREFIX = (By.ID, "edit-s-prefix")
    FILL_SHIPPING_LNAME = (By.ID, "edit-s-lastname")
    EDIT_POSTCODE = (By.ID, "edit-s-postcode")
    EDIT_HOUSENUMBER = (By.ID, "edit-s-housenr")
    EDIT_SUFFIX = (By.ID, "edit-s-suffix")
    CHOOSE_DELDATE = (By.XPATH, "//*[@id='edit-delivery-date-options']/div[1]/label")
    CHOOSE_PAYMETH = (By.CSS_SELECTOR, "#edit-payment-method > div:nth-child(1) > label")
    SUBMIT = (By.ID, "edit-submit")
    # REDEEM LOCATORS >
    CLICK_ON_REDEEM = (By.XPATH, "//*[@id='block-menu-block-3']/div/div/ul/li[2]/a")
    EDIT_CARDNUMBER = (By.ID, "edit-cardnumber-input")
    SUBMIT_CARD = (By.ID, "edit-submit")
    ALL_CARDS = (By.CSS_SELECTOR, "#edit-submit--4")



# REUSABLE CHECKOUT
class CheckoutLocators:
# FIRST STEP
    ACCEPT_COOKIE_BUTTON = (By.CLASS_NAME, "agree-button")
    SELECT_CARD = (By.CLASS_NAME, 'ui-selectmenu-status')
    CHOOSE_CARD_QUANTITY = (By.CSS_SELECTOR, "#edit-giftcard-amount-menu > li:nth-child(3) > a")
    CHOOSE_PRICE = (By.ID, "edit-giftcard-sell-price")
    ADDITION_CARD = (By.ID, "edit-addcard")
    ACCEPT_MESSAGE = (By. CSS_SELECTOR, ".ui-dialog .ui-widget-content .ui-button")
    NEXT_STEP = (By.CLASS_NAME, "fake-next-step")
    NEXT_STEP2 = (By.ID, "edit-submit")
    NEXT_STEP3 = (By.CSS_SELECTOR, ".form-actions.form-wrapper > input[type='submit']")
# VINE / WRAPPERS / MESSAGE
    VINE_BLOCK = (By.CSS_SELECTOR, ".view-wines .views-row-1 > .node-wine")
    VINE_BUTTON = (By.CSS_SELECTOR, ".view-wines .views-row-1 .field-name-amount-form-wine input[type='submit']")
    MESSAGE = (By.CSS_SELECTOR, "#edit-right .form-textarea-wrapper #edit-s-remark")
    MESSAGE_BUTTON = (By.CLASS_NAME, "add-remark")
    WRAPPER_BLOCK = (By.CSS_SELECTOR, ".view-content .views-row-1 .ds-1col")
    WRAPPER_BUTTON = (By.CSS_SELECTOR, ".ds-1col .field-items .field-item #edit-ammount-wrapper input[type='submit']")
# FILLING FORM
    NAME = (By.ID, "edit-b-initials")
    LASTNAME = (By.ID, "edit-b-lastname")
    ZIPCODE = (By.ID, "edit-b-zipcode")
    HOUSE_NUMBER = (By.ID, "edit-b-housenr")
    HOUSE_NUMBER2 = (By.CSS_SELECTOR, "span label[for='edit-b-housenr-addon']")
    PHONE = (By.ID, "edit-b-phone")
    EMAIL = (By.ID, "edit-b-email")
# CHOOSE METHOD
    IDEAL = (By.XPATH, "//div[@id='edit-payment-method']/div/div")  #   #edit-payment-method .form-item .iradio #edit-payment-method-ideal
    VISA = (By)
    MC = (By)
    INVOICE = (By)
# LAST STEP
    LAST_STEP = (By.ID, "edit-submit")
# SELECT_BANK
    SELECT_BANK_IDEAL = (By.ID, "brq_SERVICE_ideal_issuer")

    CONTINUE = (By.ID, "button_continue")
# SUBMIT STATUS
    SUBMIT = (By.XPATH, "//input[@value='Submit status']")














    @classmethod
    def all_locators(cls):
        result = []
        for atr in CBLocators.__dict__:
            if not atr.startswith("_") and atr != "all_locators":
                result.append(CBLocators.__dict__[atr])
        return result


if __name__ == "__main__":
    print(CBLocators.all_locators())

    def test_check_all_element_existace(app):
        locators = CBLocators.all_locators()
        for locator in locators:
            assert app.is_elements_present(locator)


