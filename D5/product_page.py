from appium.webdriver.common.appiumby import AppiumBy
from D5.base_page import BasePage
from D5.cart_page import CartPage

class ProductPage(BasePage):
    class Locators:
        PRODUCT_TITLE = (AppiumBy.ID, "productTV")
        PRICE = (AppiumBy.ID, "priceTV")
        QUANTITY = (AppiumBy.ID, "noTV")
        MINUS_BUTTON = (AppiumBy.ID, "minusIV")
        PLUS_BUTTON = (AppiumBy.ID, "plusIV")
        ADD_TO_CART_BUTTON = (AppiumBy.ID, "cartBt")
        CART_ICON = (AppiumBy.ID, "cartTV")
        CART_BUTTON = (AppiumBy.ID, "cartIV")

    def get_product_page_title(self):
        return self.get_element_text(*self.Locators.PRODUCT_TITLE)

    def get_product_price(self):
        return self.get_element_text(*self.Locators.PRICE)

    def get_quantity(self):
        return int(self.get_element_text(*self.Locators.QUANTITY))

    def decrease_quantity(self):
        self.click_element(*self.Locators.MINUS_BUTTON)

    def increase_quantity(self):
        self.click_element(*self.Locators.PLUS_BUTTON)

    def add_to_cart(self):
        self.click_element(*self.Locators.ADD_TO_CART_BUTTON)

    def is_add_to_cart_button_enabled(self):
        return self.find_element(*self.Locators.ADD_TO_CART_BUTTON).is_enabled()

    def get_cart_icon_count(self):
        elements = self.driver.find_elements(*self.Locators.CART_ICON)
        if len(elements) > 0:
            return int(elements[0].text)
        return 0

    def click_cart_icon(self):
        self.click_element(*self.Locators.CART_BUTTON)
        return CartPage(self.driver)