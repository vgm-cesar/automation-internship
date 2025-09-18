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
        NOTIFICATION_CARD = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"android:id/text\")")

    def click_show_popup(self):
        self.click_element(*self.Locators.SHOW_POPUP)
    
    def click_accept_option(self):
        self.click_element(*self.Locators.ACCEPT_TEXT)
    
    def click_notification_button(self):
        self.click_element(*self.Locators.NOTIFICATION_BUTTON)
        time.sleep(1)
        self.click_element(*self.Locators.ALLOW_BUTTON)
        time.sleep(0.5)
        self.click_element(*self.Locators.NOTIFICATION_BUTTON)
        time.sleep(1)

    def get_mutable_button_text(self):
        return self.get_element_text(*self.Locators.MUTABLE_BUTTON)
    
    def validate_notification(self):
        return self.is_notification_displayed(*self.Locators.NOTIFICATION_CARD)
    
    def validate_notification_text(self):
        return self.get_notification_text(*self.Locators.NOTIFICATION_CARD)