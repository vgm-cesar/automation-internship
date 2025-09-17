from appium.webdriver.common.appiumby import AppiumBy
from D5.base_page import BasePage
from D5.checkout_complete_page import CheckoutCompletePage

class ReviewOrderPage(BasePage):
    class Locators:
        CHECKOUT_TITLE = (AppiumBy.ID, "checkoutTitleTV")
        REVIEW_ORDER_TITLE = (AppiumBy.ID, "enterShippingAddressTV")
        PRODUCT_NAME = (AppiumBy.ID, "titleTV")
        PRODUCT_PRICE = (AppiumBy.ID, "priceTV")
        FULL_NAME_DELIVERY = (AppiumBy.ID, "fullNameTV")
        ADDRESS_DELIVERY = (AppiumBy.ID, "addressTV")
        CITY_DELIVERY = (AppiumBy.ID, "cityTV")
        COUNTRY_DELIVERY = (AppiumBy.ID, "countryTV")
        FULL_NAME_PAYMENT = (AppiumBy.ID, "cardHolderTV")
        CARD_NUMBER_PAYMENT = (AppiumBy.ID, "cardNumberTV")
        EXP_DATE_PAYMENT = (AppiumBy.ID, "expirationDateTV")
        TOTAL_ITEMS = (AppiumBy.ID, "itemNumberTV")
        DELIVERY_FEE = (AppiumBy.ID, "amountTV")
        TOTAL_AMOUNT = (AppiumBy.ID, "totalAmountTV")
        PLACE_ORDER_BUTTON = (AppiumBy.ID, "paymentBtn")

    def get_checkout_title(self):
        return self.get_element_text(*self.Locators.CHECKOUT_TITLE)

    def get_review_order_title(self):
        return self.get_element_text(*self.Locators.REVIEW_ORDER_TITLE)

    def get_product_name(self):
        return self.get_element_text(*self.Locators.PRODUCT_NAME)

    def get_product_price(self):
        return self.get_element_text(*self.Locators.PRODUCT_PRICE)

    def get_full_name_delivery(self):
        return self.get_element_text(*self.Locators.FULL_NAME_DELIVERY)

    def get_address_delivery(self):
        return self.get_element_text(*self.Locators.ADDRESS_DELIVERY)

    def get_city_delivery(self):
        return self.get_element_text(*self.Locators.CITY_DELIVERY)

    def get_country_delivery(self):
        return self.get_element_text(*self.Locators.COUNTRY_DELIVERY)

    def get_full_name_payment(self):
        return self.get_element_text(*self.Locators.FULL_NAME_PAYMENT)

    def get_card_number_payment(self):
        return self.get_element_text(*self.Locators.CARD_NUMBER_PAYMENT)

    def get_exp_date_payment(self):
        return self.get_element_text(*self.Locators.EXP_DATE_PAYMENT).replace("Exp: ", "")

    def get_total_number_of_items(self):
        return self.get_element_text(*self.Locators.TOTAL_ITEMS)

    def get_delivery_fee(self):
        return self.get_element_text(*self.Locators.DELIVERY_FEE).replace("$", "")

    def get_total_amount(self):
        return self.get_element_text(*self.Locators.TOTAL_AMOUNT)

    def click_place_order_button(self):
        self.click_element(*self.Locators.PLACE_ORDER_BUTTON)
        return CheckoutCompletePage(self.driver)

    def scroll_down(self):
        self.driver.swipe(300, 1500, 300, 500, duration=500)