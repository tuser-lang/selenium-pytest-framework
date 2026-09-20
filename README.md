# Selenium Pytest Automation Framework

![GitHub Actions](https://github.com/tuser-lang/selenium-pytest-framework/actions/workflows/tests.yml/badge.svg)

A Selenium WebDriver automation framework built with Python, Pytest, and the Page Object Model (POM).

The project automates the main functionality of the SauceDemo application and runs the test suite locally as well as automatically through GitHub Actions CI.

---

## 🚀 Tech Stack

- Python 3.14
- Selenium WebDriver
- Pytest
- Pytest HTML Reports
- Page Object Model (POM)
- Git & GitHub
- GitHub Actions
- Chrome / Headless Chrome

---

## 📁 Project Structure

```text
selenium-pytest-framework/
│
├── .github/
│   └── workflows/
│       └── tests.yml
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
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

Automated Tests
The framework currently contains 7 automated tests.

Login Tests
Invalid username and password
Missing username
Missing password


Product Tests
Verify product count
Add product to cart
Add product and verify cart

Framework Design
The project follows the Page Object Model design pattern.
Page-specific Selenium operations are separated from test cases.
For example:
Test
 ↓
CheckoutPage
 ↓
Selenium WebDriver
 ↓
SauceDemo

This makes the tests easier to maintain and reuse.

Installation
Clone the repository:
git clone https://github.com/tuser-lang/selenium-pytest-framework.git

Navigate to the project:
cd selenium-pytest-framework

Create a virtual environment:
python -m venv venv

Activate it on Windows:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run Tests
Run the complete test suite:
pytest -v

Run a specific test:
pytest -v tests/test_checkout.py::test_complete_checkout

Run tests by marker:
pytest -v -m smoke
or:
pytest -v -m regression

Test Reports
The project uses pytest-html to generate an HTML test report.

Run:
pytest -v --html=reports/report.html
The generated report can be opened in a browser.

Failure Screenshots
The framework automatically captures a screenshot when a test fails.
Screenshots are saved under:
screenshots/
This helps with debugging Selenium failures.

Continuous Integration
GitHub Actions runs the automated tests on:
Push to main
Pull requests targeting main
Manual workflow execution

The workflow:

Checkout code
      ↓
Set up Python
      ↓
Install dependencies
      ↓
Run Pytest
      ↓
Pass / Fail

The workflow file is:

.github/workflows/tests.yml

Manual Execution

The workflow also supports:

GitHub → Actions → Selenium Pytest Tests → Run workflow

This allows the test suite to be executed without making a new code change.


Purpose
This project demonstrates practical skills in:
Selenium WebDriver automation
Python
Pytest
Page Object Model
Test fixtures
Test parametrization
Test markers
Explicit waits
Failure screenshots
HTML reporting
Git/GitHub
CI/CD with GitHub Actions
Headless browser execution

Author
Tuser

QA Automation / Selenium / Python
When the workflow is passing, GitHub will display a green badge. If a future commit breaks the tests, it will change to a failing status.

So someone visiting your repository can immediately see:
Selenium Pytest Tests — passing ✅

