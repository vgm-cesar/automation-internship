import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:deviceName": "emulator-5554",
	"appium:automationName": "UiAutomator2",
	"appium:appPackage": "com.saucelabs.mydemoapp.android"
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(4)

el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"com.saucelabs.mydemoapp.android:id/productIV\").instance(0)")
el4.click()
time.sleep(1)
el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Green color")
el5.click()
time.sleep(1)
el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tap to add product to cart")
el6.click()
time.sleep(1)
el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(3)")
el7.click()
time.sleep(1)
el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Increase item quantity")
el8.click()
time.sleep(1)
el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Confirms products for checkout")
el9.click()
time.sleep(1)
el10 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/nameET")
el10.send_keys("TESTE")
el11 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/passwordET")
el11.send_keys("1231231231")
el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tap to login with given credentials")
el12.click()

time.sleep(5)
driver.quit()