class ProductsPage:
    def __init__(self, page):
        self.page = page

    def is_logged_in(self):
        return self.page.is_visible(".inventory_list")
        
    def get_product_list(self):
        """Return a list of products as dicts: {'name': str, 'price': str}"""
        products_list = []
        product_items = self.page.locator(".inventory_item")
        count = product_items.count()
        for i in range(count):
            name = product_items.nth(i).locator('[data-test="inventory-item-name"]').inner_text().strip()
            price = product_items.nth(i).locator('[data-test="inventory-item-price"]').inner_text().strip()
            products_list.append({"name": name, "price": price})
        return products_list

    def add_product_to_cart(self, product_name):
        product_selector = f'[data-test="inventory-item-name"]:has-text("{product_name}")'
        self.page.click(product_selector)
        self.page.get_by_role("button", name="Add to cart").click()
        self.page.get_by_role("button", name="Back to products").click()

    def get_cart_count(self):
        return self.page.inner_text(".shopping_cart_badge")