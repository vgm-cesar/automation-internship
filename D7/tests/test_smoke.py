import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
@pytest.mark.login
class TestLogin:
    def test_valid_login(self, driver):
        """
        This test verifies that a user can successfully log in.
        It's a basic check to ensure the login functionality is working.
        """
        home_page = HomePage(driver)
        product_page = home_page.select_orange_backpack()
        product_page.add_to_cart()
        cart_page = product_page.click_cart_icon()
        login_page = cart_page.click_checkout_button()

        # Perform login
        login_page.enter_username()
        login_page.enter_password()
        checkout_page = login_page.login()
        
        # Assert that we have successfully navigated to the checkout page
        assert checkout_page.get_checkout_page_title() == "Checkout"
        
    # @pytest.mark.parametrize("user", "alice@example.com") # Try without '[]'
    @pytest.mark.parametrize("user", ["alice@example.com"])
    def test_invalid_login(self, driver, user):
        """
        This test verifies that a user can successfully log in.
        It's a basic check to ensure the login functionality is working.
        """
        home_page = HomePage(driver)
        product_page = home_page.select_orange_backpack()
        product_page.add_to_cart()
        cart_page = product_page.click_cart_icon()
        login_page = cart_page.click_checkout_button()

        # Perform login
        login_page.enter_username(user)
        login_page.enter_password()
        login_page.login()
        
        # Assert that we have successfully blocked
        assert login_page.get_login_page_title() == "Login"
        assert login_page.is_password_error_displayed() == True