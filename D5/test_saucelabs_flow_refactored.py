import pytest
from D5.home_page import HomePage
from D5.data import VALID_USER, PRODUCTS

# @pytest.mark.parametrize("product_key, "user_key", [("backpack", "user_key")])
# @pytest.mark.parametrize("product_key", ["backpack"])
@pytest.mark.parametrize("product_key", ["backpack", "backpack_red"]) # Parameters passed to test function
def test_saucelabs_product_purchase_flow(driver, product_key):
    user_data = VALID_USER
    product_data = PRODUCTS[product_key]

    home_page = HomePage(driver)
    assert home_page.get_home_page_title() == "Products"

    product_page = home_page.select_orange_backpack()
    assert product_page.get_product_page_title() == product_data["name"]
    assert product_page.get_product_price() == product_data["price"]

    quantity_before_remove = product_page.get_quantity()
    product_page.decrease_quantity()
    quantity_after_remove = product_page.get_quantity()
    assert quantity_before_remove - quantity_after_remove == 1

    assert not product_page.is_add_to_cart_button_enabled()

    product_page.increase_quantity()
    quantity_after_add = product_page.get_quantity()
    assert quantity_after_remove - quantity_after_add == -1
    product_page.increase_quantity()
    assert product_page.is_add_to_cart_button_enabled()

    assert product_page.get_cart_icon_count() == 0
    product_page.add_to_cart()
    assert product_page.get_cart_icon_count() > 0
    assert product_page.get_cart_icon_count() == 2
    cart_page = product_page.click_cart_icon()

    assert cart_page.get_cart_page_title() == "My Cart"
    assert cart_page.get_product_title() == product_data["name"]
    assert cart_page.get_product_price() == product_data["price"]
    assert cart_page.get_product_quantity() == 2
    assert cart_page.get_total_items_text() == "2 Items"
    login_page = cart_page.click_checkout_button()

    assert login_page.get_login_page_title() == "Login"
    login_page.click_login_button()
    assert login_page.is_username_error_displayed()
    login_page.enter_username()
    login_page.click_login_button()
    assert login_page.is_password_error_displayed()
    login_page.enter_password()
    checkout_page = login_page.login()

    assert checkout_page.get_checkout_page_title() == "Checkout"
    payment_page = checkout_page.click_payment_button()
    assert checkout_page.is_full_name_error_displayed()
    assert checkout_page.is_address1_error_displayed()
    assert checkout_page.is_city_error_displayed()
    assert checkout_page.is_zip_error_displayed()
    assert checkout_page.is_country_error_displayed()

    checkout_page.enter_shipping_details(
        user_data["full_name_address"],
        user_data["address_line"],
        user_data["city"],
        user_data["zip_code"],
        user_data["country"]
    )
    payment_page = checkout_page.click_payment_button()

    assert payment_page.get_payment_page_title() == "Checkout"
    review_order_page = payment_page.click_payment_button()
    assert payment_page.is_name_error_displayed()
    assert payment_page.is_card_number_error_displayed()
    assert payment_page.is_expiration_date_error_displayed()
    assert payment_page.is_security_code_error_displayed()

    payment_page.enter_payment_details(
        user_data["full_name_payment"],
        user_data["card_number"],
        user_data["exp_date"],
        user_data["secure_code"]
    )
    review_order_page = payment_page.click_payment_button()

    assert review_order_page.get_checkout_title() == "Checkout"
    assert review_order_page.get_review_order_title() == "Review your order"
    assert review_order_page.get_product_name() == product_data["name"]
    assert review_order_page.get_product_price() == product_data["price"]
    assert review_order_page.get_full_name_delivery() == user_data["full_name_address"]
    assert review_order_page.get_address_delivery() == user_data["address_line"]
    assert review_order_page.get_city_delivery().strip()[:-1] == user_data["city"]
    assert review_order_page.get_country_delivery() == user_data["country"] + ', ' + user_data["zip_code"]

    review_order_page.scroll_down()

    assert review_order_page.get_full_name_payment() == user_data["full_name_payment"]
    assert review_order_page.get_card_number_payment() == user_data["card_number"]
    assert review_order_page.get_exp_date_payment() == user_data["exp_date"]
    assert review_order_page.get_total_number_of_items() == "2 Items"

    delivery_fee_checkout = float(review_order_page.get_delivery_fee())
    product_price_checkout_float = float(product_data["price"].replace("$ ", ""))
    total = delivery_fee_checkout + product_price_checkout_float * 2
    assert review_order_page.get_total_amount() == "$ " + str(total)

    checkout_complete_page = review_order_page.click_place_order_button()

    assert checkout_complete_page.get_checkout_complete_title() == "Checkout Complete"
    checkout_complete_page.click_shopping_button()

    assert home_page.get_home_page_title() == "Products"
    assert product_page.get_cart_icon_count() == 0