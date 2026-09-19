from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_product_count(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCTS)
        )
        return len(products)

    def click_add_to_cart(self, product_name):
        products = self.driver.find_elements(
            *self.PRODUCTS
        )

        for product in products:
            name = product.find_element(
                *self.PRODUCT_NAMES
            ).text

            if name == product_name:
                product.find_element(
                    By.CSS_SELECTOR,
                    "button"
                ).click()
                return

        raise ValueError(f"Product not found: {product_name}")

    def click_cart(self):
        self.driver.find_element(*self.CART_ICON).click()