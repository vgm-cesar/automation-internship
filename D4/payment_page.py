from appium.webdriver.common.appiumby import AppiumBy
from base_page import BasePage

class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.payment_title_id = "enterPaymentTitleTV"
        self.payment_button_id = "paymentBtn"
        self.name_error_id = "nameErrorIV"
        self.card_number_error_id = "cardNumberErrorIV"
        self.expiration_date_error_id = "expirationDateIV"
        self.security_code_error_id = "securityCodeIV"
        self.name_input_id = "nameET"
        self.card_number_input_id = "cardNumberET"
        self.expiration_date_input_id = "expirationDateET"
        self.security_code_input_id = "securityCodeET"

    def get_payment_page_title(self):
        return self.get_element_text(AppiumBy.ID, self.payment_title_id)

    def click_payment_button(self):
        self.click_element(AppiumBy.ID, self.payment_button_id)

    def is_name_error_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.name_error_id)

    def is_card_number_error_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.card_number_error_id)

    def is_expiration_date_error_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.expiration_date_error_id)

    def is_security_code_error_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.security_code_error_id)

    def enter_payment_details(self, full_name, card_number, exp_date, secure_code):
        self.send_keys_to_element(AppiumBy.ID, self.name_input_id, full_name)
        self.send_keys_to_element(AppiumBy.ID, self.card_number_input_id, card_number)
        self.send_keys_to_element(AppiumBy.ID, self.expiration_date_input_id, exp_date)
        self.send_keys_to_element(AppiumBy.ID, self.security_code_input_id, secure_code)