import pytest
import time
from home_page import HomePage

def test_popup_notification(driver):

    home_page = HomePage(driver)
    
    # Pop up
    # home_page.click_show_popup()
    # home_page.click_accept_option()
    # time.sleep(1)
    # assert home_page.get_mutable_button_text().strip() == "Wait 10 seconds..."
    # time.sleep(10)
    # assert home_page.get_mutable_button_text().strip() == "Text changed!"
    
    # Notification
    home_page.click_notification_button()
    assert home_page.validate_notification(), "Notification was not displayed."