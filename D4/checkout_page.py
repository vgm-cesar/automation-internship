from appium.webdriver.common.appiumby import AppiumBy
from base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_title_id = "checkoutTitleTV"
        self.payment_button_id = "paymentBtn"
        self.full_name_error_id = "fullNameErrorTV"
        self.address1_error_id = "address1ErrorTV"
        self.city_error_id = "cityErrorTV"
        self.zip_error_id = "zipErrorTV"
        self.country_error_id = "countryErrorTV"
        self.full_name_input_id = "fullNameET"
        self.address1_input_id = "address1ET"
        self.city_input_id = "cityET"
        self.zip_input_id = "zipET"
        self.country_input_id = "countryET"

    def get_checkout_page_title(self):
        return self.get_element_text(AppiumBy.ID, self.checkout_title_id)

    def click_payment_button(self):
        self.click_element(AppiumBy.ID, self.payment_button_id)

    def is_full_name_error_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.full_name_error_id)

    def is_address1_error_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.address1_error_id)

    def is_city_error_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.city_error_id)

    def is_zip_error_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.zip_error_id)

    def is_country_error_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.country_error_id)

    def enter_shipping_details(self, full_name, address_line, city, zip_code, country):
        self.send_keys_to_element(AppiumBy.ID, self.full_name_input_id, full_name)
        self.send_keys_to_element(AppiumBy.ID, self.address1_input_id, address_line)
        self.send_keys_to_element(AppiumBy.ID, self.city_input_id, city)
        self.send_keys_to_element(AppiumBy.ID, self.zip_input_id, zip_code)
        self.send_keys_to_element(AppiumBy.ID, self.country_input_id, country)