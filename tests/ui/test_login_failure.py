import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

@pytest.mark.ui
def test_unsuccessful_login(browser_launch, config):
    """Test unsuccessful login with invalid credentials."""
    page = browser_launch.new_page()
    login_page = LoginPage(page)
    login_page.open(config['BASE_URL'])
    login_page.login(config['USERNAME'], config['INVALID_PASSWORD'])  # Use invalid password from config
    
    # Wait for error message to be visible
    page.wait_for_selector('.error-message-container', state='visible')
    expect(page.locator('.error-message-container')).to_have_text("Epic sadface: Username and password do not match any user in this service")