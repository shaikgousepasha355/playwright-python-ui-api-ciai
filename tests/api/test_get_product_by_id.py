import pytest
from api_helpers.products_client import ProductsClient

@pytest.mark.api
def test_get_product_by_id(config):
    """Test GET /products/{id} for a single product."""
    product_id = 1
    api_response = ProductsClient.get_product_by_id(config['API_BASE_URL'], product_id)
    response = api_response.json()
    print(response)  # Debug print to see full response structure
    assert api_response.status_code == 200, f"Expected status code 200 but got {api_response.status_code}"
    assert response['id'] == product_id, f"Expected product ID to be {product_id}"
    assert 'id' in response and isinstance(response['id'], int), "Product ID should be an integer"
    assert 'title' in response and isinstance(response['title'], str), "Product title should be a string"
    assert 'price' in response and isinstance(response['price'], (int, float)), "Product price should be a number"
