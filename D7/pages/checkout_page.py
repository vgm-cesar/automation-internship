from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.payment_page import PaymentPage

class CheckoutPage(BasePage):
    class Locators:
        CHECKOUT_TITLE = (AppiumBy.ID, "checkoutTitleTV")
        PAYMENT_BUTTON = (AppiumBy.ID, "paymentBtn")
        FULL_NAME_ERROR = (AppiumBy.ID, "fullNameErrorTV")
        ADDRESS1_ERROR = (AppiumBy.ID, "address1ErrorTV")
        CITY_ERROR = (AppiumBy.ID, "cityErrorTV")
        ZIP_ERROR = (AppiumBy.ID, "zipErrorTV")
        COUNTRY_ERROR = (AppiumBy.ID, "countryErrorTV")
        FULL_NAME_INPUT = (AppiumBy.ID, "fullNameET")
        ADDRESS1_INPUT = (AppiumBy.ID, "address1ET")
        CITY_INPUT = (AppiumBy.ID, "cityET")
        ZIP_INPUT = (AppiumBy.ID, "zipET")
        COUNTRY_INPUT = (AppiumBy.ID, "countryET")

    def get_checkout_page_title(self):
        return self.get_element_text(*self.Locators.CHECKOUT_TITLE)

    def click_payment_button(self):
        self.click_element(*self.Locators.PAYMENT_BUTTON)
        return PaymentPage(self.driver)

    def is_full_name_error_displayed(self):
        return self.is_element_displayed(*self.Locators.FULL_NAME_ERROR)

    def is_address1_error_displayed(self):
        return self.is_element_displayed(*self.Locators.ADDRESS1_ERROR)

    def is_city_error_displayed(self):
        return self.is_element_displayed(*self.Locators.CITY_ERROR)

    def is_zip_error_displayed(self):
        return self.is_element_displayed(*self.Locators.ZIP_ERROR)

    def is_country_error_displayed(self):
        return self.is_element_displayed(*self.Locators.COUNTRY_ERROR)

    def enter_shipping_details(self, full_name, address_line, city, zip_code, country):
        self.send_keys_to_element(*self.Locators.FULL_NAME_INPUT, full_name)
        self.send_keys_to_element(*self.Locators.ADDRESS1_INPUT, address_line)
        self.send_keys_to_element(*self.Locators.CITY_INPUT, city)
        self.send_keys_to_element(*self.Locators.ZIP_INPUT, zip_code)
        self.send_keys_to_element(*self.Locators.COUNTRY_INPUT, country)