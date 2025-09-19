import pytest
from pages.home_page import HomePage
from data import VALID_USER, PRODUCTS

@pytest.mark.regression
@pytest.mark.purchase
class TestProductPurchase:
    @pytest.mark.parametrize("product_key", ["backpack"])
    def test_saucelabs_product_purchase_flow(self, driver, product_key):
        """
        This test covers the full end-to-end product purchase flow.
        It is marked as a regression test because it's a comprehensive scenario.
        """
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
        login_page = cart_page.click_checkout_button()

        assert login_page.get_login_page_title() == "Login"
        login_page.enter_username()
        login_page.enter_password()
        checkout_page = login_page.login()

        assert checkout_page.get_checkout_page_title() == "Checkout"
        checkout_page.enter_shipping_details(
            user_data["full_name_address"],
            user_data["address_line"],
            user_data["city"],
            user_data["zip_code"],
            user_data["country"]
        )
        payment_page = checkout_page.click_payment_button()

        assert payment_page.get_payment_page_title() == "Checkout"
        payment_page.enter_payment_details(
            user_data["full_name_payment"],
            user_data["card_number"],
            user_data["exp_date"],
            user_data["secure_code"]
        )
        review_order_page = payment_page.click_payment_button()

        assert review_order_page.get_checkout_title() == "Checkout"
        review_order_page.scroll_down()
        
        checkout_complete_page = review_order_page.click_place_order_button()

        assert checkout_complete_page.get_checkout_complete_title() == "Checkout Complete"
        checkout_complete_page.click_shopping_button()

        assert home_page.get_home_page_title() == "Products"
        assert product_page.get_cart_icon_count() == 0