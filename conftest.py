import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    options.add_argument("--disable-notifications")

    # Required for GitHub Actions / Linux CI
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_leak_detection": False,
            "profile.default_content_setting_values.notifications": 2,
        },
    )

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    return driver