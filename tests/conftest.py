import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def chromium_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page() 


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email_input = page.get_by_test_id('registration-form-email-input').locator('input').fill("user.name@gmail.com")
    username_input = page.get_by_test_id('registration-form-username-input').locator('input').fill("username")
    password_input = page.get_by_test_id('registration-form-password-input').locator('input').fill("password")
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    page.wait_for_url("**/dashboard")
    context.storage_state(path='browser-state.json')
    yield

@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    
    yield page