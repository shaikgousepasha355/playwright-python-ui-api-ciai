from typing import List, Dict, Optional
from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_item_selector = ".cart_item"
        self.item_name_selector = ".inventory_item_name"
        self.item_price_selector = ".inventory_item_price"

    def open(self):
        """Navigate to the cart page."""
        self.page.goto("https://www.saucedemo.com/cart.html")
        self.page.wait_for_selector(self.cart_item_selector, state="attached")

    def get_cart_items(self):
        """Return a list of items in the cart as dicts: {"name": str, "price": str}"""
        items = []
        cart_items = self.page.locator(self.cart_item_selector)
        count = cart_items.count()
        for i in range(count):
            name = cart_items.nth(i).locator(self.item_name_selector).inner_text().strip()
            price = cart_items.nth(i).locator(self.item_price_selector).inner_text().strip()
            items.append({"name": name, "price": price})
        return items

    def get_cart_total(self) -> Optional[float]:
        """Returns the sum of item prices parsed from cart items."""
        total = 0.0
        cart_items = self.page.locator(self.cart_item_selector)
        count = cart_items.count()
        for i in range(count):
            price_text = cart_items.nth(i).locator(self.item_price_selector).inner_text().strip()
            # Remove currency symbol and convert to float
            price = float(price_text.replace("$", "").replace(",", ""))
            total += price
        return round(total, 2)