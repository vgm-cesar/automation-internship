from appium.webdriver.common.appiumby import AppiumBy
from base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title_id = "productTV"
        self.title_id = "titleTV"
        self.price_id = "priceTV"
        self.quantity_id = "noTV"
        self.items_text_id = "itemsTV"
        self.checkout_button_id = "cartBt"

    def get_cart_page_title(self):
        return self.get_element_text(AppiumBy.ID, self.product_title_id)

    def get_product_title(self):
        return self.get_element_text(AppiumBy.ID, self.title_id)

    def get_product_price(self):
        return self.get_element_text(AppiumBy.ID, self.price_id)

    def get_product_quantity(self):
        return int(self.get_element_text(AppiumBy.ID, self.quantity_id))

    def get_total_items_text(self):
        return self.get_element_text(AppiumBy.ID, self.items_text_id)

    def click_checkout_button(self):
        self.click_element(AppiumBy.ID, self.checkout_button_id)