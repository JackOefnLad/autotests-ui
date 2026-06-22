import pytest
from playwright.sync_api import Page, expect # type: ignore

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    course_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_header).to_be_visible()
    expect(course_header).to_have_text('Courses')

    course_empty_block_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(course_empty_block_icon).to_be_visible()

    course_empty_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(course_empty_text).to_be_visible()
    expect(course_empty_text).to_have_text('There is no results')

    course_pipeline_result = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(course_pipeline_result).to_be_visible()
    expect(course_pipeline_result).to_have_text('Results from the load test pipeline will be displayed here')