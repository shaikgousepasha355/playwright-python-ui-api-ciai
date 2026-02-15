import pytest
from pages.login_page import LoginPage
from utils.logger import log_error, log_info

@pytest.mark.ui
def test_successful_login(browser_launch, config):
    """Test successful login with valid credentials."""
    log_info("Starting login test.")
    page = browser_launch.new_page()
    login_page = LoginPage(page)
    login_page.open(config['BASE_URL'])
    login_page.login(config['USERNAME'], config['PASSWORD'])
       
    # Wait for products page to load
    page.wait_for_selector('.inventory_list', state='visible')
    assert page.url == f"{config['BASE_URL']}inventory.html", "Expected to be redirected to the products page"
    assert page.locator('.inventory_list').is_visible(), "Products list should be visible"
    log_info("Login test completed successfully.")

    # Capture screenshot on failure
    if not page.locator('.inventory_list').is_visible():
        page.screenshot(path='failure_screenshot.png')
        log_error("Login test failed.")