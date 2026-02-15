# File: /playwright-python-ui-automation/playwright-python-ui-automation/tests/conftest.py

import pytest
from playwright.sync_api import sync_playwright
import yaml


@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)
    
@pytest.fixture(scope="session")
def browser_launch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()
