import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.ui
def test_add_products_to_cart_and_validate(browser_launch, config):
    """Test adding products to cart and validating cart contents."""
    page = browser_launch.new_page()
    login = LoginPage(page)
    # Log in
    login.open(config['BASE_URL'])
    login.login(config['USERNAME'], config['PASSWORD'])

    products = ProductsPage(page)
    
    # Wait for products page to indicate login
    assert products.is_logged_in(), "Expected to be on products page after login"

    # Choose two products
    products_list = products.get_product_list()
    assert len(products_list) >= 2, "Expected at least two products to be present on products page"

    first_product = products_list[0]["name"]
    second_product = products_list[1]["name"]
    
    # Add products to cart
    products.add_product_to_cart(first_product)
    products.add_product_to_cart(second_product)

    # Assert cart badge shows correct number
    page.wait_for_selector(f'.shopping_cart_badge:text("2")', timeout=5000)
    cart_count = int(products.get_cart_count())
    assert cart_count == 2, f"Cart badge expected to be 2 but was {cart_count}"

    # Open cart and validate items
    cart = CartPage(page)
    cart.open()
    page.wait_for_selector(".cart_item", state="visible")

    items = cart.get_cart_items()
    print(items)  # Debug print to see cart items
    item_names = [it["name"] for it in items]
    assert first_product in item_names, f"Expected '{first_product}' in cart items"
    assert second_product in item_names, f"Expected '{second_product}' in cart items"

    # Validate total
    expected_total = cart.get_cart_total()
    print(expected_total)  # Debug print to see calculated total
    assert expected_total is not None and expected_total >= 0, "Expected a non-negative cart total"