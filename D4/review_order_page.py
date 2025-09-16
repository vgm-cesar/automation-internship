from appium.webdriver.common.appiumby import AppiumBy
from base_page import BasePage

class ReviewOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_title_id = "checkoutTitleTV"
        self.review_order_title_id = "enterShippingAddressTV"
        self.product_name_id = "titleTV"
        self.product_price_id = "priceTV"
        self.full_name_delivery_id = "fullNameTV"
        self.address_delivery_id = "addressTV"
        self.city_delivery_id = "cityTV"
        self.country_delivery_id = "countryTV"
        self.full_name_payment_id = "cardHolderTV"
        self.card_number_payment_id = "cardNumberTV"
        self.exp_date_payment_id = "expirationDateTV"
        self.total_items_id = "itemNumberTV"
        self.delivery_fee_id = "amountTV"
        self.total_amount_id = "totalAmountTV"
        self.place_order_button_id = "paymentBtn"

    def get_checkout_title(self):
        return self.get_element_text(AppiumBy.ID, self.checkout_title_id)

    def get_review_order_title(self):
        return self.get_element_text(AppiumBy.ID, self.review_order_title_id)

    def get_product_name(self):
        return self.get_element_text(AppiumBy.ID, self.product_name_id)

    def get_product_price(self):
        return self.get_element_text(AppiumBy.ID, self.product_price_id)

    def get_full_name_delivery(self):
        return self.get_element_text(AppiumBy.ID, self.full_name_delivery_id)

    def get_address_delivery(self):
        return self.get_element_text(AppiumBy.ID, self.address_delivery_id)

    def get_city_delivery(self):
        return self.get_element_text(AppiumBy.ID, self.city_delivery_id)

    def get_country_delivery(self):
        return self.get_element_text(AppiumBy.ID, self.country_delivery_id)

    def get_full_name_payment(self):
        return self.get_element_text(AppiumBy.ID, self.full_name_payment_id)

    def get_card_number_payment(self):
        return self.get_element_text(AppiumBy.ID, self.card_number_payment_id)

    def get_exp_date_payment(self):
        return self.get_element_text(AppiumBy.ID, self.exp_date_payment_id).replace("Exp: ", "")

    def get_total_number_of_items(self):
        return self.get_element_text(AppiumBy.ID, self.total_items_id)

    def get_delivery_fee(self):
        return self.get_element_text(AppiumBy.ID, self.delivery_fee_id).replace("$", "")

    def get_total_amount(self):
        return self.get_element_text(AppiumBy.ID, self.total_amount_id)

    def click_place_order_button(self):
        self.click_element(AppiumBy.ID, self.place_order_button_id)

    def scroll_down(self):
        self.driver.swipe(300, 1500, 300, 500, duration=500)