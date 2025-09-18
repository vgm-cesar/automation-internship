import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to take a screenshot on test failure.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            # Create a unique filename for the screenshot
            screenshot_name = f"screenshot_{item.name}.png"
            try:
                driver.get_screenshot_as_file(screenshot_name)
                print(f"Screenshot saved as {screenshot_name}")
            except Exception as e:
                print(f"Failed to take screenshot: {e}")

@pytest.fixture(scope="function")
def driver():
    """
    Appium driver fixture for Android.
    """
    _driver = None
    try:
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
    except Exception as e:
        pytest.skip(f"Failed to create Appium driver: {e}")

    yield _driver

    if _driver:
        _driver.quit()