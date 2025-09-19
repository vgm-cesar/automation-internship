from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.product_page import ProductPage

class HomePage(BasePage):
    class Locators:
        PRODUCT_TITLE = (AppiumBy.ID, "productTV")
        ORANGE_BACKPACK = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Product Title' and @text='Sauce Labs Backpack (orange)']/../android.widget.ImageView")

    def get_home_page_title(self):
        return self.get_element_text(*self.Locators.PRODUCT_TITLE)

    def select_orange_backpack(self):
        self.click_element(*self.Locators.ORANGE_BACKPACK)
        return ProductPage(self.driver)