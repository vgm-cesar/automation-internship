from appium.webdriver.common.appiumby import AppiumBy
from D5.base_page import BasePage

class CheckoutCompletePage(BasePage):
    class Locators:
        COMPLETE_TITLE = (AppiumBy.ID, "completeTV")
        SHOPPING_BUTTON = (AppiumBy.ID, "shoopingBt")

    def get_checkout_complete_title(self):
        return self.get_element_text(*self.Locators.COMPLETE_TITLE)

    def click_shopping_button(self):
        self.click_element(*self.Locators.SHOPPING_BUTTON)
