from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    # Установка фокуса на поле ввода
    email_input.focus()

    for char in 'user@gmail.com':
        page.keyboard.type(char, delay=100)
        # page.keyboard.press(char, delay=300)

    # Выделение текста через Ctrl+A
    page.keyboard.press('ControlOrMeta+A')


    page.wait_for_timeout(5000)