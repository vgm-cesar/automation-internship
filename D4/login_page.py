from appium.webdriver.common.appiumby import AppiumBy
from base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_title_id = "loginTV"
        self.login_button_id = "loginBtn"
        self.username_error_id = "nameErrorTV"
        self.password_error_id = "passwordErrorTV"
        self.username_input_id = "nameET"
        self.password_input_id = "passwordET"
        self.username_text_id = "username1TV"
        self.password_text_id = "password1TV"

    def get_login_page_title(self):
        return self.get_element_text(AppiumBy.ID, self.login_title_id)

    def click_login_button(self):
        self.click_element(AppiumBy.ID, self.login_button_id)

    def is_username_error_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.username_error_id)

    def is_password_error_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.password_error_id)

    def enter_username(self, username=None):
        if username is None:
            username = self.get_element_text(AppiumBy.ID, self.username_text_id)
        self.send_keys_to_element(AppiumBy.ID, self.username_input_id, username)

    def enter_password(self, password=None):
        if password is None:
            password = self.get_element_text(AppiumBy.ID, self.password_text_id)
        self.send_keys_to_element(AppiumBy.ID, self.password_input_id, password)

    def login(self, username=None, password=None):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()