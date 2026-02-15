import requests
from utils.logger import log_info, log_error

class ProductsClient:
    """Client for interacting with the Products API."""

    def get_all_products(API_BASE_URL):
        """Fetch all products from the API."""
        log_info("Fetching all products from API.")
        try:
            response = requests.get(API_BASE_URL)
            response.raise_for_status()
            log_info("Successfully fetched all products.")
            return response
        except requests.HTTPError as e:
            log_error(f"Error fetching products: {e}")

    def get_product_by_id(API_BASE_URL, product_id):
        """Fetch a single product by ID."""
        log_info(f"Fetching product with ID: {product_id}.")
        try:
            response = requests.get(f"{API_BASE_URL}/{product_id}")
            response.raise_for_status()
            log_info(f"Successfully fetched product ID: {product_id}.")
            return response
        except requests.HTTPError as e:
            log_error(f"Error fetching product ID {product_id}: {e}")