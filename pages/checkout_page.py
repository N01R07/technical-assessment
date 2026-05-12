from playwright.sync_api import Page, expect
import pytest

class CheckoutPage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.title_header = page.get_by_text("Your Cart")
        self.cart_btn = page.locator("[data-test=\"shopping-cart-link\"]")
        self.checkout_btn = page.get_by_role("button", name="Checkout")
        self.finalize_checkout_btn = page.locator("[data-test=\"continue\"]")
        self.finish_checkout_btn = page.locator("[data-test=\"finish\"]")
    
    def verifyCheckoutPage(self):
        try:
            expect(self.title_header).to_be_visible()
        except:
            pytest.fail("Failed to navigate to checkout page! Or 'Your Cart' header is not visible!")
    
    def clickcart(self):
        self.cart_btn.click()

    def clickCheckout(self):
        self.checkout_btn.click()
    
    def finalizeCheckout(self):
        self.finalize_checkout_btn.click()
    
    def finishCheckout(self):
        self.finish_checkout_btn.click()
    
