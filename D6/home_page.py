from appium.webdriver.common.appiumby import AppiumBy
from D6.base_page import BasePage
import time

class HomePage(BasePage):
    class Locators:
        SHOW_POPUP = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Show Popup\")")
        ACCEPT_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"Accept\"]")
        NOTIFICATION_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Notification\")")
        ALLOW_BUTTON = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        MUTABLE_BUTTON = (AppiumBy.XPATH, "(//android.widget.TextView)[3]") # Note the button doesn't have a text property, only the text view.
        NOTIFICATION_CARD = (AppiumBy.XPATH, "//*[@resource-id=\"android:id/text\"]")

    def click_show_popup(self):
        return self.click_element(*self.Locators.SHOW_POPUP)
    
    def click_accept_option(self):
        return self.click_element(*self.Locators.ACCEPT_TEXT)
    
    def click_notification_button(self):
        self.click_element(*self.Locators.NOTIFICATION_BUTTON)
        time.sleep(1)
        return self.click_element(*self.Locators.ALLOW_BUTTON)

    def get_mutable_button_text(self):
        return self.get_element_text(*self.Locators.MUTABLE_BUTTON)
    
    def validate_notification(self):
        return self.is_notification_displayed(*self.Locators.NOTIFICATION_CARD)
    
    
    # pip3 install uiautodev
    
    
    # uiauto.dev
    
    # Remember to close the Appium Inspector instance