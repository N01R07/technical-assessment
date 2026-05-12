from playwright.sync_api import Page, expect
import pytest

class CheckoutInformationPage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.title_header = page.get_by_text("Checkout: Your Information")
        self.username_input = page.get_by_role("textbox", name="First Name")
        self.password_input = page.get_by_role("textbox", name="Last Name")
        self.code_input = page.get_by_role("textbox", name="Zip/Postal code")
        self.checkout_btn = page.get_by_role("button", name="Checkout")
    
    def verifyCheckoutPage(self):
        try:
            expect(self.title_header).to_be_visible()
        except:
            pytest.fail("Failed to navigate to checkout page! Or 'Your Cart' header is not visible!")

    def setFirstName(self, first_name: str):
        self.username_input.fill(first_name)

    def setLastName(self, last_name: str):
        self.password_input.fill(last_name)

    def setCode(self, code: str):
        self.code_input.fill(code)
    
    def clickCheckout(self):
        self.checkout_btn.click()
    
