from playwright.sync_api import sync_playwright # type: ignore

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    # page.keyboard.insert_text("Тест моментального ввода")
    # page.keyboard.down("Digit9")
    # page.keyboard.type("World", delay=100)
    
    for character in "user@mail.com":
        page.keyboard.press(character, delay=300)

    page.keyboard.press("ControlOrMeta+A")
    page.wait_for_timeout(5000)
    browser.close()
