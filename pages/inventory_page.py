from playwright.sync_api import Page, expect
import pytest

class InventoryPage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.title_header = page.get_by_text("Products")
        self.backpack_btn = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.bike_light = page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        self.bolt_t_shirt = page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")
        self.fleece_jacket = page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")
        self.onesie = page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]")
        self.all_the_things_shirt = page.locator("[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]")

    def verifyInventoryPage(self):
        try:
            expect(self.title_header).to_be_visible()
        except:
            pytest.fail("Failed to login! Or 'Products' header is not visible!")
    
    def click_backpack_AddToCart(self):
        self.backpack_btn.click()
    
    def click_bike_light_AddToCart(self):
        self.bike_light.click()
    
    def click_bolt_t_shirt_AddToCart(self):
        self.bolt_t_shirt.click()
    
    def click_fleece_jacket_AddToCart(self):
        self.fleece_jacket.click()
    
    def click_onesie_AddToCart(self):
        self.onesie.click()
    
    def click_shirt_AddToCart(self):
        self.all_the_things_shirt.click()

    
    
