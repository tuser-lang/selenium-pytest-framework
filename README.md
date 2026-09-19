# Selenium Pytest Automation Framework

A Python Selenium automation framework using Pytest and Page Object Model (POM).

## Features

- Selenium WebDriver automation
- Pytest test framework
- Page Object Model
- Reusable fixtures
- Parameterized tests
- Login testing
- Product testing
- Cart testing
- Checkout testing
- Automatic screenshots on test failure
- HTML test reports

## Project Structure

```text
selenium-pytest-framework/
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
├── reports/
│
├── conftest.py
├── requirements.txt
└── README.md