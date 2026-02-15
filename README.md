# Playwright Python UI Automation

This project is a test automation suite for the SauceDemo web application and public dummyjson product APIs using Playwright and pytest. It includes both UI and API tests, following best practices for test design and quality requirements.

## Prerequisites

- Python 3.7 or higher
- Node.js (for Playwright installation)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd playwright-python-ui-automation
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:
   ```
   playwright install
   ```

## Running Tests

You can run the tests using pytest. Here are some commands you can use:

- To run all tests:
  ```
  pytest
  ```

- To run tests in parallel:
  ```
  pytest -n auto
  ```  

- To run only UI tests:
  ```
  pytest tests/ui
  ```

- To run only API tests:
  ```
  pytest tests/api
  ```

## Folder Structure

playwright-python-ui-automation/
├── README.md
├── requirements.txt
├── pytest.ini
├── config/ # Configuration files
│ └── config.py # Contains credentials and base URLs
├── api_helpers/ # API client for interacting with the Products API
│ └── products_client.py
├── fixtures/ # Test data and fixtures
│ └── test_data.py
├── pages/ # Page Object Model for UI interactions
│ ├── base_page.py
│ ├── cart_page.py
│ ├── login_page.py
│ └── product_page.py
├── tests/ # Test cases
│ ├── api/ # API tests
│ │ ├── test_get_all_products.py
│ │ ├── test_get_product_by_id.py
│ │ └── test_get_product_by_invalid_id.py
│ ├── ui/ # UI tests
│ │ ├── test_login_success.py
│ │ ├── test_login_failure.py
│ │ └── test_add_to_cart.py
│ ├── test_ui_api_consistency.py
│ ├── conftest.py
└── utils/ # Utility functions
│  └── logger.py # Logging utility

## Logging
 ```
 The project includes a logging utility that logs key actions such as API requests and login attempts. Logs are printed to the console.
 ```

## CI Integration
 ```
 To integrate this test suite into a CI pipeline (e.g., GitHub Actions), you can create a workflow file in the .github/workflows directory. Create a file named python-tests.yml in .github/workflows/ with the following content:
```

name: playwright-python-ui-api-automation

on: [push, pull_request]

jobs:
  test:
    runs-on: OS (windows/ubuntu) latest
    steps:
      - name: Checkout code
        uses: actions/checkout

      - name: Set up Python
        uses: actions/setup-python
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest -n auto  # Run tests in parallel