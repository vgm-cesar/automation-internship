from appium.webdriver.common.appiumby import AppiumBy
from base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title_id = "productTV"
        self.price_id = "priceTV"
        self.quantity_id = "noTV"
        self.minus_button_id = "minusIV"
        self.plus_button_id = "plusIV"
        self.add_to_cart_button_id = "cartBt"
        self.cart_icon_id = "cartTV"
        self.cart_button_id = "cartIV"

    def get_product_page_title(self):
        return self.get_element_text(AppiumBy.ID, self.product_title_id)

    def get_product_price(self):
        return self.get_element_text(AppiumBy.ID, self.price_id)

    def get_quantity(self):
        return int(self.get_element_text(AppiumBy.ID, self.quantity_id))

    def decrease_quantity(self):
        self.click_element(AppiumBy.ID, self.minus_button_id)

    def increase_quantity(self):
        self.click_element(AppiumBy.ID, self.plus_button_id)

    def add_to_cart(self):
        self.click_element(AppiumBy.ID, self.add_to_cart_button_id)

    def is_add_to_cart_button_enabled(self):
        return self.driver.find_element(AppiumBy.ID, self.add_to_cart_button_id).is_enabled()

    def get_cart_icon_count(self):
        elements = self.driver.find_elements(AppiumBy.ID, self.cart_icon_id)
        if len(elements) > 0:
            return int(elements[0].text)
        return 0

    def click_cart_icon(self):
        self.click_element(AppiumBy.ID, self.cart_button_id)