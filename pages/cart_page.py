from typing import List, Dict, Optional
from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_item_selector = ".cart_item"
        self.item_name_selector = ".inventory_item_name"
        self.item_price_selector = ".inventory_item_price"
        # summary subtotal (present on checkout/summary pages). Attempt to read if available.
        self.summary_subtotal_selector = ".summary_subtotal_label"

    def open(self):
        """Navigate to the cart page."""
        self.page.goto("https://www.saucedemo.com/cart.html")
        self.page.wait_for_selector(self.cart_item_selector, state="attached")

    def get_cart_items(self):
        """Return a list of items in the cart as dicts: {"name": str, "price": str}"""
        items = []
        # ensure items are present (if none, returns empty list)
        elements = self.page.query_selector_all(self.cart_item_selector)
        for el in elements:
            name_el = el.query_selector(self.item_name_selector)
            price_el = el.query_selector(self.item_price_selector)
            name = name_el.inner_text().strip() if name_el else ""
            price = price_el.inner_text().strip() if price_el else ""
            items.append({"name": name, "price": price})
        return items

    def get_cart_total(self) -> Optional[float]:
        """Returns the sum of item prices parsed from cart items."""
        items = self.get_cart_items()
        total = 0.0
        for it in items:
            # remove currency symbols and commas
            import re
            price_text = it.get("price", "")
            m = re.search(r"([0-9]+(?:\.[0-9]+)?)", price_text)
            if m:
                total += float(m.group(1))
        return round(total, 2)