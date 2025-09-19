import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
import base64
import os
from utils.logger import log

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
            screenshot_dir = "screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            screenshot_name = f"{screenshot_dir}/screenshot_{item.name}.png"
            try:
                driver.get_screenshot_as_file(screenshot_name)
                log.debug(f"Screenshot saved as {screenshot_name}")
            except Exception as e:
                log.debug(f"Failed to take screenshot: {e}")

@pytest.fixture(scope="function")
def driver(request):
    """
    Appium driver fixture for Android.
    Includes video recording for the test session.
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
        _driver.start_recording_screen()
    except Exception as e:
        pytest.skip(f"Failed to create Appium driver: {e}")

    yield _driver

    if _driver:
        video_data = _driver.stop_recording_screen()
        if video_data:
            video_dir = "videos"
            if not os.path.exists(video_dir):
                os.makedirs(video_dir)
            video_filename = f"{video_dir}/video_{request.node.name}.mp4"
            with open(video_filename, "wb") as f:
                f.write(base64.b64decode(video_data))
            log.debug(f"Video saved as {video_filename}")
        _driver.quit()