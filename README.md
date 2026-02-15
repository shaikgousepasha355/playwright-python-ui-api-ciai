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

## Configuration

Edit config.yaml to set your credentials and base URLs:
 ```
  USERNAME: "standard_user"
  PASSWORD: "secret_sauce"
  INVALID_PASSWORD: "wrong_password"
  BASE_URL: "https://www.saucedemo.com/"
  API_BASE_URL: "https://dummyjson.com/products"
 ```

## Running Tests

You can run the tests using pytest. Here are some commands you can use:

- To run all tests:
  ```
  pytest --html=report.html
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

- `pages/`: Page Object Model classes for UI
- `tests/ui`: UI test cases
- `tests/api`: API test cases
- `utils/`: logging
- `conftest.py`: Pytest fixtures
- `config/`: YAML config files
- `api_helpers/`: api product client helpers(methods)

## Notes
- Mapping Strategy: Since SauceDemo and DummyJSON products do not match one-to-one, I've validated structural aspect (types and presence of fields) rather than exact values across systems.
- If there is direct mapping - like product names/titles and prices match between SauceDemo UI and DummyJSON API,I've provided commented test logic that assert exact value equality.
- See comments in test_ui_api_consistency.py for details.

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

        - name: Install Playwright browsers
          run: |
            python -m playwright install

        - name: Run tests
          run: |
            pytest -n auto  # Run tests in parallel