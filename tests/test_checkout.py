from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.regression
def test_complete_checkout(logged_in_driver):

    # Add product
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.click_add_to_cart(
        "Sauce Labs Backpack"
    )

    # Go to cart
    inventory_page.click_cart()

    # Checkout
    cart_page = CartPage(logged_in_driver)

    cart_page.click_checkout()

    # Enter customer information
    checkout_page = CheckoutPage(logged_in_driver)
    checkout_page.enter_first_name("John")
    checkout_page.enter_last_name("Doe")
    checkout_page.enter_postal_code("629001")
    

    

    checkout_page.click_continue()

    

    


    


    # Finish order
    checkout_page.click_finish()

    # Verify order completion
    
    assert "checkout-complete.html" in logged_in_driver.current_url

    assert checkout_page.get_complete_message() == "Thank you for your order!"