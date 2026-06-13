from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context()
    #     page = context.new_page()
    #
    #     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    #
    #     email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    #     email_input.fill('user.name@gmail.com')
    #
    #     username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    #     username_input.fill('username')
    #
    #     password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    #     password_input.fill('password')
    #
    #     register_button = page.get_by_test_id('registration-page-registration-button')
    #     register_button.click()
    #
    #     context.storage_state(path='test_data.json')
    #
    #     page.wait_for_timeout(3000)
    #
    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context(storage_state='test_data.json')
    #     page = context.new_page()

        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        course_title_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(course_title_text).to_be_visible()
        expect(course_title_text).to_have_text('Courses')

        empty_title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(empty_title_text).to_be_visible()
        expect(empty_title_text).to_have_text('There is no results')

        empty_course_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_course_icon).to_be_visible()

        course_empty_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(course_empty_description).to_be_visible()
        expect(course_empty_description).to_have_text('Results from the load test pipeline will be displayed here')

        chromium_page_with_state.wait_for_timeout(3000)