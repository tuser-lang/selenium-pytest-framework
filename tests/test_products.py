from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest

@pytest.mark.smoke
def test_product_count(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page = InventoryPage(driver)

    product_count = inventory_page.get_product_count()

    assert product_count == 6

@pytest.mark.regression
def test_add_product_to_cart(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page = InventoryPage(driver)

    inventory_page.click_add_to_cart(
        "Sauce Labs Backpack"
    )

    inventory_page.click_cart()

    assert "cart.html" in driver.current_url
    
@pytest.mark.regression
def test_add_product_and_verify_cart(logged_in_driver):

    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.click_add_to_cart(
        "Sauce Labs Backpack"
    )

    inventory_page.click_cart()

    cart_page = CartPage(logged_in_driver)

    item_count = cart_page.get_cart_item_count()
    
    assert item_count == 1


    