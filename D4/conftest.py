import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions

@pytest.fixture(scope="function")
def driver():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.saucelabs.mydemoapp.android",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })
    _driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield _driver
    _driver.quit()