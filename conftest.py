import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": { "width": 1280, "height": 720 },
    }

@pytest.fixture
def page(browser):
   page = browser.new_page()
   yield page
   page.close()