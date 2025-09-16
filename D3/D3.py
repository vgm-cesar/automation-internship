import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from selenium.webdriver.common.by import By

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

productName = "Sauce Labs Backpack (orange)"
productPrice = "$ 29.99"
fullNameAddress = "Full Name"
fullNamePayment = "Full Name"
adressLine = "Address Line 1"
city = "City"
country = "Country"
zipCode = "12345"
cardNumber = "12345678"
secureCode = "123"
expDate = "01/01"

homePageTitleExpected = "Products"
myCartPageTitleExpected = "My Cart"
loginPageTitleExpected = "Login"
checkoutPageTitleExpected = "Checkout"
checkoutPaymentPageTitleExpected = "Checkout"
reviewYourOrderPageTitleExpected = "Review your order"
checkoutCompletePageTitleExpected = "Checkout Complete"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(2)

# Validate HomePage
homePageTitle = driver.find_element(By.ID, "productTV").text
assert homePageTitle == homePageTitleExpected, f"Incorret 'Home Page' Title. Actual: '{homePageTitle}' - Expected: '{homePageTitleExpected}'"

# Select the 'Sauce Labs Backpack (orange)' product
driver.find_element(By.XPATH, f"//android.widget.TextView[@content-desc='Product Title' and @text='{productName}']/../android.widget.ImageView").click()
time.sleep(1)

# Validate Product Page Title
productPageTitle = driver.find_element(By.ID, "productTV").text
assert productPageTitle == productName, f"Incorret 'Product Page' Title. Actual: '{productPageTitle}' - Expected: '{productName}'"

# Validate Product Price
productPrice = driver.find_element(By.ID, "priceTV").text
assert productPrice == productPrice, f"Incorret Product Price. Actual: '{productPrice}' - Expected: '{productPrice}'"

# Validate removing product units
quantityBeforeRemove = driver.find_element(By.ID, "noTV").text
driver.find_element(By.ID, "minusIV").click()
time.sleep(0.5)
quantityAfterRemove = driver.find_element(By.ID, "noTV").text
time.sleep(0.5)
assert int(quantityBeforeRemove) - int(quantityAfterRemove) == 1, f"Incorret Product Quantity after Removing. Actual: '{quantityAfterRemove}' - Expected: '{str(int(quantityBeforeRemove)-1)}'"

# Validate addToCart Button
assert not driver.find_element(By.ID, "cartBt").is_enabled(), f"'Add to cart' button is enabled with zero products."

# Validate Adding product units
driver.find_element(By.ID, "plusIV").click()
quantityAfterAdd = driver.find_element(By.ID, "noTV").text
assert int(quantityAfterRemove) - int(quantityAfterAdd) == -1, f"Incorret Product Quantity after Adding. Actual: '{quantityAfterRemove}' - Expected: '{str(int(quantityBeforeRemove)-1)}'"
driver.find_element(By.ID, "plusIV").click()
time.sleep(0.5)
assert driver.find_element(By.ID, "cartBt").is_enabled(), f"'Add to cart' button is disabled with more than zero products."

# Validate Cart Icon element
assert len(driver.find_elements(By.ID, "cartTV")) == 0, f"Element containing number of products on cart is visible."
driver.find_element(By.ID, "cartBt").click()
time.sleep(0.5)
assert len(driver.find_elements(By.ID, "cartTV")) > 0, f"Element containing number of products on cart is not visible."
assert driver.find_element(By.ID, "cartTV").text == "2", f"Number of products on cart icon is wrong."
driver.find_element(By.ID, "cartIV").click()
time.sleep(0.5)

# My Cart Page
myCartTitle = driver.find_element(By.ID, "productTV").text
assert myCartTitle == myCartPageTitleExpected, f"Incorret 'My Cart' Page Title. Actual: '{myCartTitle}' - Expected: '{myCartPageTitleExpected}'"

productTitle = driver.find_element(By.ID, "titleTV").text
assert productTitle == productName, f"Incorret Product Name. Actual: '{productTitle}' - Expected: '{productName}'"

myCartProductPrice = driver.find_element(By.ID, "priceTV").text
assert productPrice == myCartProductPrice, f"Incorret Product Price. Actual: '{myCartProductPrice}' - Expected: '{productPrice}'"

myCartProductPrice = driver.find_element(By.ID, "priceTV").text
assert productPrice == myCartProductPrice, f"Incorret Product Price. Actual: '{myCartProductPrice}' - Expected: '{productPrice}'"

myCartQuantity = driver.find_element(By.ID, "noTV").text
assert int(myCartQuantity) == 2, f"Incorret Product Quantity. Actual: '{myCartQuantity}' - Expected: '2'"

myCartTotalQuantity = driver.find_element(By.ID, "itemsTV").text
assert myCartTotalQuantity == "2 Items", f"Incorret Total Product Quantity. Actual: '{myCartTotalQuantity}' - Expected: '2'"
driver.find_element(By.ID, "cartBt").click()
time.sleep(0.5)

# Login Page
loginPageTitle = driver.find_element(By.ID, "loginTV").text
assert loginPageTitle == loginPageTitleExpected, f"Incorret 'Login' Page Title. Actual: '{loginPageTitle}' - Expected: '{loginPageTitleExpected}'"

driver.find_element(By.ID, "loginBtn").click()
time.sleep(0.5)
assert len(driver.find_elements(By.ID, "nameErrorTV")) > 0, f"'Username is required' message is not visible."

driver.find_element(By.ID, "nameET").send_keys(driver.find_element(By.ID, "username1TV").text)
driver.find_element(By.ID, "loginBtn").click()
time.sleep(0.5)
assert len(driver.find_elements(By.ID, "passwordErrorTV")) > 0, f"'Enter Password' message is not visible."
driver.find_element(By.ID, "passwordET").send_keys(driver.find_element(By.ID, "password1TV").text)
driver.find_element(By.ID, "loginBtn").click()
time.sleep(0.5)

# Checkout Page
checkoutPageTitle = driver.find_element(By.ID, "checkoutTitleTV").text
assert checkoutPageTitle == checkoutPageTitleExpected, f"Incorret 'Checkout' Page Title. Actual: '{checkoutPageTitle}' - Expected: '{checkoutPageTitleExpected}'"

driver.find_element(By.ID, "paymentBtn").click()
time.sleep(1)
assert len(driver.find_elements(By.ID, "fullNameErrorTV")) > 0, f"'Please provide your full name' message is not visible."
assert len(driver.find_elements(By.ID, "address1ErrorTV")) > 0, f"'Please provide your address' message is not visible."
assert len(driver.find_elements(By.ID, "cityErrorTV")) > 0, f"'Please provide your city' message is not visible."
assert len(driver.find_elements(By.ID, "zipErrorTV")) > 0, f"'Please provide your zip' message is not visible."
assert len(driver.find_elements(By.ID, "countryErrorTV")) > 0, f"'Please provide your' message is not visible."

driver.find_element(By.ID, "fullNameET").send_keys(fullNameAddress)
driver.find_element(By.ID, "address1ET").send_keys(adressLine)
driver.find_element(By.ID, "cityET").send_keys(city)
driver.find_element(By.ID, "zipET").send_keys(zipCode)
driver.find_element(By.ID, "countryET").send_keys(country)
driver.find_element(By.ID, "paymentBtn").click()
time.sleep(1)

# Checkout Payment Page
checkoutPaymentPageTitle = driver.find_element(By.ID, "enterPaymentTitleTV").text
assert checkoutPaymentPageTitle == checkoutPaymentPageTitleExpected, f"Incorret 'Checkout Payment' Page Title. Actual: '{checkoutPaymentPageTitle}' - Expected: '{checkoutPaymentPageTitleExpected}'"

driver.find_element(By.ID, "paymentBtn").click()
time.sleep(1)

assert len(driver.find_elements(By.ID, "nameErrorIV")) > 0, f"'Full Name' icon error is not visible."
assert len(driver.find_elements(By.ID, "cardNumberErrorIV")) > 0, f"'Card Number' icon error is not visible."
assert len(driver.find_elements(By.ID, "expirationDateIV")) > 0, f"'Expiration Date' icon error is not visible."
assert len(driver.find_elements(By.ID, "securityCodeIV")) > 0, f"'Security Code' icon error is not visible."

driver.find_element(By.ID, "nameET").send_keys(fullNamePayment)
driver.find_element(By.ID, "cardNumberET").send_keys(cardNumber)
driver.find_element(By.ID, "expirationDateET").send_keys(expDate)
driver.find_element(By.ID, "securityCodeET").send_keys(secureCode)
driver.find_element(By.ID, "paymentBtn").click()
time.sleep(1)

# Checkout, Review your order
checkoutPageTitle = driver.find_element(By.ID, "checkoutTitleTV").text
assert checkoutPageTitle == checkoutPageTitleExpected, f"Incorret 'Checkout' Page Title. Actual: '{checkoutPageTitle}' - Expected: '{checkoutPageTitleExpected}'"

reviewYourOrderPageTitle = driver.find_element(By.ID, "enterShippingAddressTV").text
assert reviewYourOrderPageTitle == reviewYourOrderPageTitleExpected, f"Incorret 'Checkout, Review your order' Page Title. Actual: '{reviewYourOrderPageTitle}' - Expected: '{reviewYourOrderPageTitleExpected}'"

## Deliver Address
productNameCheckout = driver.find_element(By.ID, "titleTV").text
assert productNameCheckout == productName, f"Incorret Product Name on Checkout Page. Actual: '{productNameCheckout}' - Expected: '{productName}'"

productPriceCheckout = driver.find_element(By.ID, "priceTV").text
assert productPriceCheckout == productPrice, f"Incorret Product Price on Checkout Page. Actual: '{productPriceCheckout}' - Expected: '{productPrice}'"

fullNameDeliverCheckout = driver.find_element(By.ID, "fullNameTV").text
assert fullNameDeliverCheckout == fullNameAddress, f"Incorret Full Name on Checkout Review you Order Page (Deliver). Actual: '{fullNameDeliverCheckout}' - Expected: '{fullNameAddress}'"

addressDelivery = driver.find_element(By.ID, "addressTV").text
assert addressDelivery == adressLine, f"Incorret Address Line on Checkout Review you Order Page. Actual: '{addressDelivery}' - Expected: '{adressLine}'"

cityDelivery = driver.find_element(By.ID, "cityTV").text
assert cityDelivery.strip()[:-1] == city, f"Incorret City on Checkout Review you Order Page. Actual: '{cityDelivery}' - Expected: '{city}'"

countryDelivery = driver.find_element(By.ID, "countryTV").text
assert countryDelivery == country+', '+zipCode, f"Incorret Country and/or Zipcode on Checkout Review you Order Page. Actual: '{countryDelivery}' - Expected: '{country+', '+zipCode}'"

# Perform a scroll down to view Payment Method and Delivery Fee
driver.swipe(300, 1500, 300, 500, duration=500)

## Payment Method
fullNamePaymentCheckout = driver.find_element(By.ID, "cardHolderTV").text
assert fullNamePaymentCheckout == fullNamePayment, f"Incorret Full Name on Checkout Review you Order Page (Payment). Actual: '{fullNamePaymentCheckout}' - Expected: '{fullNamePayment}'"

cardNumberPaymentCheckout = driver.find_element(By.ID, "cardNumberTV").text
assert cardNumberPaymentCheckout == cardNumber, f"Incorret Card Number on Checkout Review you Order Page (Payment). Actual: '{cardNumberPaymentCheckout}' - Expected: '{cardNumber}'"

expDatePaymentCheckout = (driver.find_element(By.ID, "expirationDateTV").text).replace("Exp: ", "")
assert expDatePaymentCheckout == expDate, f"Incorret Exp Date on Checkout Review you Order Page (Payment). Actual: '{expDatePaymentCheckout}' - Expected: '{expDate}'"

## Total
totalNumberOfItems = driver.find_element(By.ID, "itemNumberTV").text
assert totalNumberOfItems == "2 Items", f"Incorret Total Number of Items on Checkout Review you Order Page (Payment). Actual: '{totalNumberOfItems}' - Expected: '2 Items'"

deliveryFeeCheckout = (driver.find_element(By.ID, "amountTV").text).replace("$", "")
productPriceCheckout = productPriceCheckout.replace("$ ", "")
total = float(deliveryFeeCheckout) + float(productPriceCheckout)*2

totalPrice = driver.find_element(By.ID, "totalAmountTV").text
assert totalPrice == "$ "+str(total), f"Incorret Total Price on Checkout Review you Order Page (Payment). Actual: '{totalPrice}' - Expected: '{str(total)}'"

driver.find_element(By.ID, "paymentBtn").click()
time.sleep(1)

## Checkout Complete
checkoutCompletePageTitle = driver.find_element(By.ID, "completeTV").text
assert checkoutCompletePageTitle == checkoutCompletePageTitleExpected, f"Incorret 'Checkout Complete' Page Title. Actual: '{checkoutCompletePageTitle}' - Expected: '{checkoutCompletePageTitleExpected}'"

driver.find_element(By.ID, "shoopingBt").click()
time.sleep(3)

## Products Page
homePageTitle = driver.find_element(By.ID, "productTV").text
assert homePageTitle == homePageTitleExpected, f"Incorret 'Home Page' Title. Actual: '{homePageTitle}' - Expected: '{homePageTitleExpected}'"

assert len(driver.find_elements(By.ID, "cartTV")) == 0, f"Element containing number of products on cart is not visible."

time.sleep(3)
driver.quit()