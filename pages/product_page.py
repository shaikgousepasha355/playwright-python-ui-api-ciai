class ProductsPage:
    def __init__(self, page):
        self.page = page

    def is_logged_in(self):
        return self.page.is_visible(".inventory_list")
        
    def get_product_list(self):
        return self.page.query_selector_all(".inventory_item")

    def add_product_to_cart(self, product_name):
        product_selector = f'[data-test="inventory-item-name"]:has-text("{product_name}")'
        self.page.click(product_selector)
        self.page.get_by_role("button", name="Add to cart").click()
        self.page.get_by_role("button", name="Back to products").click()

    def get_cart_count(self):
        return self.page.inner_text(".shopping_cart_badge")