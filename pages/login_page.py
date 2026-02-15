from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
    
    def open(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.fill("input[name='user-name']", username)
        self.page.fill("input[name='password']", password)
        self.page.click("input[type='submit']")

    def get_error_message(self):
        error_message_element = self.page.query_selector(self.error_message_selector)
        if error_message_element:
            return error_message_element.inner_text()
        return None