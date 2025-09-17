from appium.webdriver.common.appiumby import AppiumBy
from D5.base_page import BasePage
from D5.login_page import LoginPage

class CartPage(BasePage):
    class Locators:
        PRODUCT_TITLE = (AppiumBy.ID, "productTV")
        TITLE = (AppiumBy.ID, "titleTV")
        PRICE = (AppiumBy.ID, "priceTV")
        QUANTITY = (AppiumBy.ID, "noTV")
        ITEMS_TEXT = (AppiumBy.ID, "itemsTV")
        CHECKOUT_BUTTON = (AppiumBy.ID, "cartBt")

    def get_cart_page_title(self):
        return self.get_element_text(*self.Locators.PRODUCT_TITLE)

    def get_product_title(self):
        return self.get_element_text(*self.Locators.TITLE)

    def get_product_price(self):
        return self.get_element_text(*self.Locators.PRICE)

    def get_product_quantity(self):
        return int(self.get_element_text(*self.Locators.QUANTITY))

    def get_total_items_text(self):
        return self.get_element_text(*self.Locators.ITEMS_TEXT)

    def click_checkout_button(self):
        self.click_element(*self.Locators.CHECKOUT_BUTTON)
        return LoginPage(self.driver)