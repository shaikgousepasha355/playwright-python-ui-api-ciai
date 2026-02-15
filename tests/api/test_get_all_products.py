import pytest
from api_helpers.products_client import ProductsClient

@pytest.mark.api
def test_get_all_products(config):
    """Test GET /products for basic validation."""
    api_response = ProductsClient.get_all_products(config['API_BASE_URL'])
    assert api_response.status_code == 200, f"Expected status code 200 but got {api_response.status_code}"
    response = api_response.json()
    assert 'products' in response, "Response should contain 'products' key"
    assert isinstance(response['products'], list), "Expected 'products' to be a list"
    assert len(response['products']) > 0, "Expected at least one product in the list"

    # Validate fields for the first product
    first_product = response['products'][0]
    assert 'id' in first_product and isinstance(first_product['id'], int), "Product ID should be an integer"
    assert 'title' in first_product and isinstance(first_product['title'], str), "Product title should be a string"
    assert 'price' in first_product and isinstance(first_product['price'], (int, float)), "Product price should be a number"
