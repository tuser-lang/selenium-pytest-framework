import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.parametrize(
    "username,password",
    [
        ("wrong_user", "wrong_password"),
        ("", "secret_sauce"),
        ("standard_user", ""),
    ]
)
def test_invalid_login(driver, username, password):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(username, password)

    error = driver.find_element(
        "css selector",
        "[data-test='error']"
    )

    assert error.is_displayed()