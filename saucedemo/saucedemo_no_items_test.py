""""
This is a test file for the checkout process of the saucedemo website. 
It performs the following steps:
1. Logs in with valid credentials.
2. Verifies that the inventory page is displayed.
3. Proceeds to the checkout page.
4. Fills in the checkout information and finalizes the checkout process.

## FAILS because items aren't added to the cart!
"""
from playwright.sync_api import Page, expect
import pytest
from conftest import page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.checkout_information import CheckoutInformationPage
from utils.screenshot import take_screenshot

def test_checkout(page: Page):
    # Initialize page objects
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    checkout_info_page = CheckoutInformationPage(page)
    test_id = "saucedemo_no_items_test"

    # Login to the application
    page.goto("https://www.saucedemo.com/")
    login_page.username_input.fill("standard_user")
    login_page.password_input.fill("secret_sauce")
    login_page.clickLogin()

    # Verify login and inventory page
    login_page.verifyLogin()
    inventory_page.verifyInventoryPage()
    
    # Proceed to checkout
    checkout_page.clickcart()

    # take_screenshot(page, 3, f"0 - {test_id}_before_checkout") # uncomment if you want to see screenshot
    
    checkout_page.verifyCheckoutPage()
    checkout_page.clickCheckout()

    # Fill in checkout information and finalize checkout
    checkout_info_page.verifyCheckoutPage()
    checkout_info_page.setFirstName("John")
    checkout_info_page.setLastName("Doe")
    checkout_info_page.setCode("12345")
    checkout_page.finalizeCheckout()
    checkout_page.finishCheckout()

    # take_screenshot(page, 3, f"1 - {test_id}_after_finalizing_checkout") # uncomment if you want to see screenshot

    expect(page.locator("[data-test='error']")).to_be_visible()