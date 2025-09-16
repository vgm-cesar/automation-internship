from appium.webdriver.common.appiumby import AppiumBy
from base_page import BasePage

class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.complete_title_id = "completeTV"
        self.shopping_button_id = "shoopingBt"

    def get_checkout_complete_title(self):
        return self.get_element_text(AppiumBy.ID, self.complete_title_id)

    def click_shopping_button(self):
        self.click_element(AppiumBy.ID, self.shopping_button_id)