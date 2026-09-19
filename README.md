# Selenium Pytest Automation Framework

A UI test automation framework built using **Python, Selenium WebDriver, and Pytest**.

The framework follows the **Page Object Model (POM)** design pattern and includes automated test execution through **GitHub Actions CI**.

## Tech Stack

- Python 3.14
- Selenium WebDriver
- Pytest
- Pytest HTML
- Git & GitHub
- GitHub Actions
- Chrome / ChromeDriver

## Project Structure

```text
selenium-pytest-framework/
│
├── .github/
│   └── workflows/
│       └── selenium-tests.yml
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   └── test_checkout.py
│
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

Application Under Test
The framework automates the following website:
SauceDemo
https://www.saucedemo.com/
The tests cover login, product selection, cart functionality, and checkout.

Test Coverage
Login Tests
Invalid username and password
Missing username
Missing password

Product Tests
Verify product count
Add product to cart
Verify product in cart

Checkout Test
Add product to cart
Navigate to checkout
Enter customer information
Continue checkout
Complete order
Verify order confirmation

Page Object Model
The project uses the Page Object Model (POM) pattern.
Each application page has its own Python class containing:
Locators
Page actions
Synchronization/waits

For example:
LoginPage
InventoryPage
CartPage
CheckoutPage

This keeps test cases clean and makes the framework easier to maintain.

Running Tests Locally
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd selenium-pytest-framework

2. Create a virtual environment
python -m venv venv

3. Activate the virtual environment

Windows:
venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Run all tests
pytest -v

6. Run a specific test
pytest -v tests/test_checkout.py::test_complete_checkout

7. Run tests by marker
Run regression tests:
pytest -v -m regression

HTML Test Report
The project uses pytest-html to generate an HTML test report.
Run:
pytest -v --html=reports/report.html
The report will be generated under:
reports/report.html

Screenshots
Screenshots are automatically captured when a test fails.
Screenshots are stored in:
screenshots/

Continuous Integration
The project uses GitHub Actions for continuous integration.
The workflow:

The workflow:

Checks out the repository
Sets up Python
Installs project dependencies
Starts Chrome in headless mode
Executes the Pytest test suite

The workflow runs automatically when code is pushed to the main branch or when a pull request targets main.

CI Configuration
Chrome is configured for headless execution in conftest.py:
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

This allows Selenium tests to run in the GitHub Actions Ubuntu environment without opening a visible browser.

Test Results
Current test suite:

7 tests
7 passed

Author
Amal

This project demonstrates practical experience with:

Selenium WebDriver
Python
Pytest
Page Object Model
Test fixtures
Parameterized testing
Test markers
HTML reporting
Git/GitHub
GitHub Actions CI