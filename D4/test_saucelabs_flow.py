from home_page import HomePage
from product_page import ProductPage
from cart_page import CartPage
from login_page import LoginPage
from checkout_page import CheckoutPage
from payment_page import PaymentPage
from review_order_page import ReviewOrderPage
from checkout_complete_page import CheckoutCompletePage
import time

class TestSauceLabsFlow:
    product_name = "Sauce Labs Backpack (orange)"
    product_price = "$ 29.99"
    full_name_address = "Full Name"
    full_name_payment = "Full Name"
    address_line = "Address Line 1"
    city = "City"
    country = "Country"
    zip_code = "12345"
    card_number = "12345678"
    secure_code = "123"
    exp_date = "01/01"

    home_page_title_expected = "Products"
    my_cart_page_title_expected = "My Cart"
    login_page_title_expected = "Login"
    checkout_page_title_expected = "Checkout"
    checkout_payment_page_title_expected = "Checkout"
    review_your_order_page_title_expected = "Review your order"
    checkout_complete_page_title_expected = "Checkout Complete"

    def test_saucelabs_product_purchase_flow(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)
        checkout_page = CheckoutPage(driver)
        payment_page = PaymentPage(driver)
        review_order_page = ReviewOrderPage(driver)
        checkout_complete_page = CheckoutCompletePage(driver)

        # Validate HomePage
        time.sleep(3)
        assert home_page.get_home_page_title() == self.home_page_title_expected, \
            f"Incorrect 'Home Page' Title. Actual: '{home_page.get_home_page_title()}' - Expected: '{self.home_page_title_expected}'"

        # Select the 'Sauce Labs Backpack (orange)' product
        home_page.select_orange_backpack()
        time.sleep(1)

        # Validate Product Page Title
        assert product_page.get_product_page_title() == self.product_name, \
            f"Incorrect 'Product Page' Title. Actual: '{product_page.get_product_page_title()}' - Expected: '{self.product_name}'"

        # Validate Product Price
        assert product_page.get_product_price() == self.product_price, \
            f"Incorrect Product Price. Actual: '{product_page.get_product_price()}' - Expected: '{self.product_price}'"

        # Validate removing product units
        quantity_before_remove = product_page.get_quantity()
        product_page.decrease_quantity()
        time.sleep(0.5)
        quantity_after_remove = product_page.get_quantity()
        time.sleep(0.5)
        assert quantity_before_remove - quantity_after_remove == 1, \
            f"Incorrect Product Quantity after Removing. Actual: '{quantity_after_remove}' - Expected: '{str(quantity_before_remove - 1)}'"

        # Validate addToCart Button
        assert not product_page.is_add_to_cart_button_enabled(), \
            f"'Add to cart' button is enabled with zero products."

        # Validate Adding product units
        product_page.increase_quantity()
        quantity_after_add = product_page.get_quantity()
        assert quantity_after_remove - quantity_after_add == -1, \
            f"Incorrect Product Quantity after Adding. Actual: '{quantity_after_add}' - Expected: '{str(quantity_after_remove + 1)}'"
        product_page.increase_quantity()
        time.sleep(0.5)
        assert product_page.is_add_to_cart_button_enabled(), \
            f"'Add to cart' button is disabled with more than zero products."

        # Validate Cart Icon element
        assert product_page.get_cart_icon_count() == 0, \
            f"Element containing number of products on cart is visible."
        product_page.add_to_cart()
        time.sleep(0.5)
        assert product_page.get_cart_icon_count() > 0, \
            f"Element containing number of products on cart is not visible."
        assert product_page.get_cart_icon_count() == 2, \
            f"Number of products on cart icon is wrong."
        product_page.click_cart_icon()
        time.sleep(0.5)

        # My Cart Page
        assert cart_page.get_cart_page_title() == self.my_cart_page_title_expected, \
            f"Incorrect 'My Cart' Page Title. Actual: '{cart_page.get_cart_page_title()}' - Expected: '{self.my_cart_page_title_expected}'"

        assert cart_page.get_product_title() == self.product_name, \
            f"Incorrect Product Name. Actual: '{cart_page.get_product_title()}' - Expected: '{self.product_name}'"

        assert cart_page.get_product_price() == self.product_price, \
            f"Incorrect Product Price. Actual: '{cart_page.get_product_price()}' - Expected: '{self.product_price}'"

        assert cart_page.get_product_quantity() == 2, \
            f"Incorrect Product Quantity. Actual: '{cart_page.get_product_quantity()}' - Expected: '2'"

        assert cart_page.get_total_items_text() == "2 Items", \
            f"Incorrect Total Product Quantity. Actual: '{cart_page.get_total_items_text()}' - Expected: '2'"
        cart_page.click_checkout_button()
        time.sleep(0.5)

        # Login Page
        assert login_page.get_login_page_title() == self.login_page_title_expected, \
            f"Incorrect 'Login' Page Title. Actual: '{login_page.get_login_page_title()}' - Expected: '{self.login_page_title_expected}'"

        login_page.click_login_button()
        time.sleep(0.5)
        assert login_page.is_username_error_displayed(), \
            f"'Username is required' message is not visible."

        login_page.enter_username()
        login_page.click_login_button()
        time.sleep(0.5)
        assert login_page.is_password_error_displayed(), \
            f"'Enter Password' message is not visible."
        login_page.enter_password()
        login_page.click_login_button()
        time.sleep(0.5)

        # Checkout Page
        assert checkout_page.get_checkout_page_title() == self.checkout_page_title_expected, \
            f"Incorrect 'Checkout' Page Title. Actual: '{checkout_page.get_checkout_page_title()}' - Expected: '{self.checkout_page_title_expected}'"

        checkout_page.click_payment_button()
        time.sleep(1)
        assert checkout_page.is_full_name_error_displayed(), \
            f"'Please provide your full name' message is not visible."
        assert checkout_page.is_address1_error_displayed(), \
            f"'Please provide your address' message is not visible."
        assert checkout_page.is_city_error_displayed(), \
            f"'Please provide your city' message is not visible."
        assert checkout_page.is_zip_error_displayed(), \
            f"'Please provide your zip' message is not visible."
        assert checkout_page.is_country_error_displayed(), \
            f"'Please provide your' message is not visible."

        checkout_page.enter_shipping_details(self.full_name_address, self.address_line, self.city, self.zip_code, self.country)
        checkout_page.click_payment_button()
        time.sleep(1)

        # Checkout Payment Page
        assert payment_page.get_payment_page_title() == self.checkout_payment_page_title_expected, \
            f"Incorrect 'Checkout Payment' Page Title. Actual: '{payment_page.get_payment_page_title()}' - Expected: '{self.checkout_payment_page_title_expected}'"

        payment_page.click_payment_button()
        time.sleep(1)

        assert payment_page.is_name_error_displayed(), \
            f"'Full Name' icon error is not visible."
        assert payment_page.is_card_number_error_displayed(), \
            f"'Card Number' icon error is not visible."
        assert payment_page.is_expiration_date_error_displayed(), \
            f"'Expiration Date' icon error is not visible."
        assert payment_page.is_security_code_error_displayed(), \
            f"'Security Code' icon error is not visible."

        payment_page.enter_payment_details(self.full_name_payment, self.card_number, self.exp_date, self.secure_code)
        payment_page.click_payment_button()
        time.sleep(1)

        # Checkout, Review your order
        assert review_order_page.get_checkout_title() == self.checkout_page_title_expected, \
            f"Incorrect 'Checkout' Page Title. Actual: '{review_order_page.get_checkout_title()}' - Expected: '{self.checkout_page_title_expected}'"

        assert review_order_page.get_review_order_title() == self.review_your_order_page_title_expected, \
            f"Incorrect 'Checkout, Review your order' Page Title. Actual: '{review_order_page.get_review_order_title()}' - Expected: '{self.review_your_order_page_title_expected}'"

        ## Deliver Address
        assert review_order_page.get_product_name() == self.product_name, \
            f"Incorrect Product Name on Checkout Page. Actual: '{review_order_page.get_product_name()}' - Expected: '{self.product_name}'"

        assert review_order_page.get_product_price() == self.product_price, \
            f"Incorrect Product Price on Checkout Page. Actual: '{review_order_page.get_product_price()}' - Expected: '{self.product_price}'"

        assert review_order_page.get_full_name_delivery() == self.full_name_address, \
            f"Incorrect Full Name on Checkout Review you Order Page (Deliver). Actual: '{review_order_page.get_full_name_delivery()}' - Expected: '{self.full_name_address}'"

        assert review_order_page.get_address_delivery() == self.address_line, \
            f"Incorrect Address Line on Checkout Review you Order Page. Actual: '{review_order_page.get_address_delivery()}' - Expected: '{self.address_line}'"

        assert review_order_page.get_city_delivery().strip()[:-1] == self.city, \
            f"Incorrect City on Checkout Review you Order Page. Actual: '{review_order_page.get_city_delivery()}' - Expected: '{self.city}'"

        assert review_order_page.get_country_delivery() == self.country + ', ' + self.zip_code, \
            f"Incorrect Country and/or Zipcode on Checkout Review you Order Page. Actual: '{review_order_page.get_country_delivery()}' - Expected: '{self.country + ', ' + self.zip_code}'"

        # Perform a scroll down to view Payment Method and Delivery Fee
        review_order_page.scroll_down()
        time.sleep(0.5)

        ## Payment Method
        assert review_order_page.get_full_name_payment() == self.full_name_payment, \
            f"Incorrect Full Name on Checkout Review you Order Page (Payment). Actual: '{review_order_page.get_full_name_payment()}' - Expected: '{self.full_name_payment}'"

        assert review_order_page.get_card_number_payment() == self.card_number, \
            f"Incorrect Card Number on Checkout Review you Order Page (Payment). Actual: '{review_order_page.get_card_number_payment()}' - Expected: '{self.card_number}'"

        assert review_order_page.get_exp_date_payment() == self.exp_date, \
            f"Incorrect Exp Date on Checkout Review you Order Page (Payment). Actual: '{review_order_page.get_exp_date_payment()}' - Expected: '{self.exp_date}'"

        ## Total
        assert review_order_page.get_total_number_of_items() == "2 Items", \
            f"Incorrect Total Number of Items on Checkout Review you Order Page (Payment). Actual: '{review_order_page.get_total_number_of_items()}' - Expected: '2 Items'"

        delivery_fee_checkout = float(review_order_page.get_delivery_fee())
        product_price_checkout_float = float(self.product_price.replace("$ ", ""))
        total = delivery_fee_checkout + product_price_checkout_float * 2

        assert review_order_page.get_total_amount() == "$ " + str(total), \
            f"Incorrect Total Price on Checkout Review you Order Page (Payment). Actual: '{review_order_page.get_total_amount()}' - Expected: '${total}'"

        review_order_page.click_place_order_button()
        time.sleep(1)

        ## Checkout Complete
        assert checkout_complete_page.get_checkout_complete_title() == self.checkout_complete_page_title_expected, \
            f"Incorrect 'Checkout Complete' Page Title. Actual: '{checkout_complete_page.get_checkout_complete_title()}' - Expected: '{self.checkout_complete_page_title_expected}'"

        checkout_complete_page.click_shopping_button()
        time.sleep(3)

        ## Products Page
        assert home_page.get_home_page_title() == self.home_page_title_expected, \
            f"Incorrect 'Home Page' Title. Actual: '{home_page.get_home_page_title()}' - Expected: '{self.home_page_title_expected}'"

        assert product_page.get_cart_icon_count() == 0, \
            f"Element containing number of products on cart is visible."
        time.sleep(3)