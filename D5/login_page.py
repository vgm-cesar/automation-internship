from appium.webdriver.common.appiumby import AppiumBy
from D5.base_page import BasePage
from D5.checkout_page import CheckoutPage

class LoginPage(BasePage):
    class Locators:
        LOGIN_TITLE = (AppiumBy.ID, "loginTV")
        LOGIN_BUTTON = (AppiumBy.ID, "loginBtn")
        USERNAME_ERROR = (AppiumBy.ID, "nameErrorTV")
        PASSWORD_ERROR = (AppiumBy.ID, "passwordErrorTV")
        USERNAME_INPUT = (AppiumBy.ID, "nameET")
        PASSWORD_INPUT = (AppiumBy.ID, "passwordET")
        USERNAME_TEXT = (AppiumBy.ID, "username1TV")
        PASSWORD_TEXT = (AppiumBy.ID, "password1TV")

    def get_login_page_title(self):
        return self.get_element_text(*self.Locators.LOGIN_TITLE)

    def click_login_button(self):
        self.click_element(*self.Locators.LOGIN_BUTTON)

    def is_username_error_displayed(self):
        return self.is_element_displayed(*self.Locators.USERNAME_ERROR)

    def is_password_error_displayed(self):
        return self.is_element_displayed(*self.Locators.PASSWORD_ERROR)

    def enter_username(self, username=None):
        if username is None:
            username = self.get_element_text(*self.Locators.USERNAME_TEXT)
        self.send_keys_to_element(*self.Locators.USERNAME_INPUT, username)

    def enter_password(self, password=None):
        if password is None:
            password = self.get_element_text(*self.Locators.PASSWORD_TEXT)
        self.send_keys_to_element(*self.Locators.PASSWORD_INPUT, password)

    def login(self):
        self.click_login_button()
        return CheckoutPage(self.driver)