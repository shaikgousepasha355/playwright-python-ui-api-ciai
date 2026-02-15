import pytest
import requests

@pytest.mark.api
def test_get_product_by_invalid_id(config):
    """Test GET /products/{id} with an invalid ID."""
    invalid_id = 99999  # Assuming this ID does not exist
    response = requests.get(f"{config['API_BASE_URL']}/{invalid_id}")
    assert response.status_code == 404  # Expecting a 404 Not Found response for an invalid ID
    assert response.json() == {"message": f"Product with id '{invalid_id}' not found"}, "Expected error message for invalid product ID"