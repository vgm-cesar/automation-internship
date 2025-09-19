from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import log

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, locator):
        log.debug(f"Finding element with locator: ('{by}', '{locator}')")
        try:
            element = self.wait.until(EC.presence_of_element_located((by, locator)))
            log.debug("Element found successfully.")
            return element
        except Exception:
            log.error(f"Element not found with locator: ('{by}', '{locator}')", exc_info=True)
            raise

    def wait_for_element_to_be_clickable(self, by, locator):
        log.debug(f"Waiting for element to be clickable: ('{by}', '{locator}')")
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, locator)))
            log.debug("Element is clickable.")
            return element
        except Exception:
            log.error(f"Element not clickable: ('{by}', '{locator}')", exc_info=True)
            raise

    def wait_for_visibility_of_element(self, by, locator):
        log.debug(f"Waiting for visibility of element: ('{by}', '{locator}')")
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, locator)))
            log.debug("Element is visible.")
            return element
        except Exception:
            log.error(f"Element not visible: ('{by}', '{locator}')", exc_info=True)
            raise

    def click_element(self, by, locator):
        log.info(f"Clicking element: ('{by}', '{locator}')")
        self.wait_for_element_to_be_clickable(by, locator).click()

    def send_keys_to_element(self, by, locator, text):
        log.info(f"Sending keys '{text}' to element: ('{by}', '{locator}')")
        element = self.wait_for_visibility_of_element(by, locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by, locator):
        log.info(f"Getting text from element: ('{by}', '{locator}')")
        return self.wait_for_visibility_of_element(by, locator).text

    def is_element_displayed(self, by, locator):
        log.info(f"Checking if element is displayed: ('{by}', '{locator}')")
        try:
            self.wait_for_visibility_of_element(by, locator)
            return True
        except TimeoutException:
            log.warning(f"Element not displayed: ('{by}', '{locator}')")
            return False