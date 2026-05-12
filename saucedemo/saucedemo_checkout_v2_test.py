""""
This test case verifies the checkout process on the SauceDemo website. It performs the following steps:
1. Logs in with valid credentials.
2. Verifies that the inventory page is displayed.
3. Adds all items to the cart.
4. Proceeds to the checkout page.
5. Fills in the checkout information and finalizes the checkout process.
"""
from playwright.sync_api import Page
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
    test_id = "saucedemo_checkout_test_v2"

    # Login to the application
    page.goto("https://www.saucedemo.com/")
    login_page.username_input.fill("standard_user")
    login_page.password_input.fill("secret_sauce")
    take_screenshot(page, 1, f"0 - {test_id}_before_login")
    login_page.clickLogin()

    # Verify login and inventory page
    login_page.verifyLogin()
    inventory_page.verifyInventoryPage()

    # Add all items to the cart
    inventory_page.click_backpack_AddToCart()
    inventory_page.click_bike_light_AddToCart()
    inventory_page.click_bolt_t_shirt_AddToCart()
    inventory_page.click_fleece_jacket_AddToCart()
    inventory_page.click_onesie_AddToCart()
    inventory_page.click_shirt_AddToCart()

    # take_screenshot(page, 1, f"1 - {test_id}_after_adding_items") # uncomment if you want to see screenshot
    
    # Proceed to checkout
    checkout_page.clickcart()
    checkout_page.verifyCheckoutPage()
    checkout_page.clickCheckout()

    # Fill in checkout information and finalize checkout
    checkout_info_page.verifyCheckoutPage()
    checkout_info_page.setFirstName("John")
    checkout_info_page.setLastName("Doe")
    checkout_info_page.setCode("12345")

    # take_screenshot(page, 1, f"2 - {test_id}_before_finalizing_checkout") # uncomment if you want to see screenshot

    # Finalize checkout
    checkout_page.finalizeCheckout()
    checkout_page.finishCheckout()

    # take_screenshot(page, 1, f"3 - {test_id}_after_finish_checkout") # uncomment if you want to see screenshot