from playwright.sync_api import sync_playwright, expect # type: ignore

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input').fill("user.name@gmail.com")
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input').fill("username")
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input').fill("password")

    expect(registration_button).to_be_enabled()

    page.wait_for_timeout(5000)
    browser.close()