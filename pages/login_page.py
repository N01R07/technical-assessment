from playwright.sync_api import Page, expect
import pytest

class LoginPage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.error_message = page.locator(".error-message-container.error")
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def setUsername(self, username: str):
        self.username_input.fill(username)

    def setPassword(self, password: str):
        self.password_input.fill(password)

    def clickLogin(self):
        self.login_button.click()
    
    def verifyLogin(self):
        try:
            expect(self.error_message).not_to_be_visible()
        except:
            pytest.fail("Failed to login!")