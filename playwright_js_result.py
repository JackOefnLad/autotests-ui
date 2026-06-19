from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'
    )

    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)

    title_result = page.evaluate("document.getElementById('authentication-ui-course-title-text').textContent")
    assert title_result == 'New Text', f"Ошибка: заголовок = '{title_result}', ожидалось 'New Text'"

    page.evaluate("""
    const registration_button = document.getElementById('login-page-registration-link');
    registration_button.textContent ='Registration';
                  """)

    button_result = page.evaluate("document.getElementById('login-page-registration-link').textContent")
    assert button_result == 'Registration', f"Ошибка: кнопка = '{button_result}', ожидалось 'Registration'"

    result_text = f"""Результаты проверки JS:
Заголовок: '{title_result}' (ожидалось: 'New Text')
Кнопка регистрации: '{button_result}' (ожидалось: 'Registration')
Все проверки пройдены успешно!
"""
    print(result_text)

    page.wait_for_timeout(5000)
    browser.close()
