from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def click_element(self, by, locator):
        self.find_element(by, locator).click()

    def send_keys_to_element(self, by, locator, text):
        self.find_element(by, locator).send_keys(text)

    def get_element_text(self, by, locator):
        return self.find_element(by, locator).text

    def is_element_displayed(self, by, locator):
        return self.find_element(by, locator)