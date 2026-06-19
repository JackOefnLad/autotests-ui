import pytest
from playwright.sync_api import sync_playwright, expect # type: ignore

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
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
        context.storage_state(path='reg-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='reg-state.json')

        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        course_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(course_header).to_be_visible()
        expect(course_header).to_have_text('Courses')

        course_empty_block_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(course_empty_block_icon).to_be_visible()

        course_empty_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(course_empty_text).to_be_visible()
        expect(course_empty_text).to_have_text('There is no results')

        course_pipeline_result = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(course_pipeline_result).to_be_visible()
        expect(course_pipeline_result).to_have_text('Results from the load test pipeline will be displayed here')