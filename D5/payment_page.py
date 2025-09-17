from appium.webdriver.common.appiumby import AppiumBy
from D5.base_page import BasePage
from D5.review_order_page import ReviewOrderPage

class PaymentPage(BasePage):
    class Locators:
        PAYMENT_TITLE = (AppiumBy.ID, "enterPaymentTitleTV")
        PAYMENT_BUTTON = (AppiumBy.ID, "paymentBtn")
        NAME_ERROR = (AppiumBy.ID, "nameErrorIV")
        CARD_NUMBER_ERROR = (AppiumBy.ID, "cardNumberErrorIV")
        EXPIRATION_DATE_ERROR = (AppiumBy.ID, "expirationDateIV")
        SECURITY_CODE_ERROR = (AppiumBy.ID, "securityCodeIV")
        NAME_INPUT = (AppiumBy.ID, "nameET")
        CARD_NUMBER_INPUT = (AppiumBy.ID, "cardNumberET")
        EXPIRATION_DATE_INPUT = (AppiumBy.ID, "expirationDateET")
        SECURITY_CODE_INPUT = (AppiumBy.ID, "securityCodeET")

    def get_payment_page_title(self):
        return self.get_element_text(*self.Locators.PAYMENT_TITLE)

    def click_payment_button(self):
        self.click_element(*self.Locators.PAYMENT_BUTTON)
        return ReviewOrderPage(self.driver)

    def is_name_error_displayed(self):
        return self.is_element_displayed(*self.Locators.NAME_ERROR)

    def is_card_number_error_displayed(self):
        return self.is_element_displayed(*self.Locators.CARD_NUMBER_ERROR)

    def is_expiration_date_error_displayed(self):
        return self.is_element_displayed(*self.Locators.EXPIRATION_DATE_ERROR)

    def is_security_code_error_displayed(self):
        return self.is_element_displayed(*self.Locators.SECURITY_CODE_ERROR)

    def enter_payment_details(self, full_name, card_number, exp_date, secure_code):
        self.send_keys_to_element(*self.Locators.NAME_INPUT, full_name)
        self.send_keys_to_element(*self.Locators.CARD_NUMBER_INPUT, card_number)
        self.send_keys_to_element(*self.Locators.EXPIRATION_DATE_INPUT, exp_date)
        self.send_keys_to_element(*self.Locators.SECURITY_CODE_INPUT, secure_code)