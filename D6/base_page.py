from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def wait_for_element_to_be_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def wait_for_visibility_of_element(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def click_element(self, by, locator):
        self.wait_for_element_to_be_clickable(by, locator).click()

    def send_keys_to_element(self, by, locator, text):
        self.wait_for_visibility_of_element(by, locator).send_keys(text)

    def get_element_text(self, by, locator):
        return self.wait_for_visibility_of_element(by, locator).text

    def is_element_displayed(self, by, locator):
        self.wait_for_visibility_of_element(by, locator)
        return True

    def open_notifications(self):
        self.driver.open_notifications()

    def is_notification_displayed(self, by, locator):
        self.wait_for_visibility_of_element(by, locator)
        return True

    def get_notification_text(self, by, locator, expected_title):
        title_element = self.wait_for_visibility_of_element(by, locator)
        notification_text = title_element.find_element(by, locator).text
        return notification_text