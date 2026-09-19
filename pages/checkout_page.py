from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):

        field = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME)
        )

        field.clear()
        field.send_keys(first_name)

        

    def enter_last_name(self, last_name):

        field = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME)
        )

        field.clear()
        field.send_keys(last_name)

        

    def enter_postal_code(self, postal_code):

        field = self.wait.until(
        EC.element_to_be_clickable(self.POSTAL_CODE)
    )

        field.clear()
        field.send_keys(postal_code)

        
        
    

    def click_continue(self):

        continue_button = self.wait.until(
        EC.element_to_be_clickable(self.CONTINUE_BUTTON)
    )

        
    

        

        continue_button.click()

        self.wait.until(
        EC.url_contains("checkout-step-two.html")
    )

    def click_finish(self):

        finish = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )

        finish.click()

        self.wait.until(
            EC.url_contains("checkout-complete.html")
        )

    def get_complete_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.COMPLETE_MESSAGE
            )
        ).text