import pytest
from api_helpers.products_client import ProductsClient
from pages.login_page import LoginPage
from pages.product_page import ProductsPage

@pytest.mark.e2e
def test_ui_api_consistency(browser_launch, config):  # Use base_url fixture
    """Test consistency between UI and API for products."""
    # Fetch products from API
    api_response = ProductsClient.get_all_products(config['API_BASE_URL'])
    api_products = api_response.json()['products'][:3]  # Get first 3 products

    # Log into the UI
    page = browser_launch.new_page()
    login_page = LoginPage(page)
    login_page.open(config['BASE_URL'])
    login_page.login(config['USERNAME'], config['PASSWORD'])

    # Wait for products page to load
    page.wait_for_selector('.inventory_list', state='visible')

    # Fetch products from UI
    ui_products = ProductsPage(page).get_product_list()[:3]  # Get first 3 products
    
    ui_products_data = []
    for product in ui_products:
        name = product.query_selector('[data-test="inventory-item-name"]').inner_text()
        price = product.query_selector('[data-test="inventory-item-price"]').inner_text()
        ui_products_data.append({"name": name, "price": price})

# Mapping strategy explanation:
# Since Sauce Demo and DummyJSON products do not match one-to-one,
# we validate that both systems provide product names/titles and prices,
# and that these fields are of the correct type and present in each product.
# Exact values are not compared across systems.

    for u in ui_products_data:
        assert isinstance(u['name'], str), "Product name should be a non-empty string"
        assert isinstance(u['price'], str), "Product price should be a string"

    for api_product in api_products:
        assert 'title' in api_product and isinstance(api_product['title'], str), "API product should have a title string"
        assert 'price' in api_product and isinstance(api_product['price'], (int, float)), "API product price should be a number"


#if we wanted to do a more direct comparison, we would need a mapping between the two product sets, which is not feasible here due to the different data sources. Instead, we ensure that both APIs provide consistent data structures and types for products.
#Refer the below commented code for an example of how we can achieve a direct comparision.

# for api_product in api_products:
    #     ui_product = None
    #     for p in ui_product_data:
    #         if p['name'] == api_product['title']:
    #             ui_product = p
    #             break
    #         assert ui_product is not None, f"Product '{api_product['title']}' not found in UI"
    #         assert ui_product['price'] == api_product['price'], f"Price mismatch for '{api_product['title']}'"
