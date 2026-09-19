import os

import pytest
from selenium import webdriver

from pages.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    options.add_argument("--disable-notifications")

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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver is None:
            driver = item.funcargs.get("logged_in_driver")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}.png"
            )

            driver.save_screenshot(screenshot_path)

            