from playwright.sync_api import sync_playwright # type: ignore

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'  # Ждем полной загрузки страницы
    )

    # Выполняем JS-код для замены текста заголовка
    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)

    # Проверяем, что значение заголовка стало равно установленному
    title_result = page.evaluate("document.getElementById('authentication-ui-course-title-text').textContent")

    page.evaluate("""
    const registration_button = document.getElementById('login-page-registration-link');
    registration_button.textContent ='Registration';
                  """)

    # Проверяем, что значение кнопки стало равно установленному
    button_result = page.evaluate("document.getElementById('login-page-registration-link').textContent")

    # Формируем результат
    result_text = f"""Результаты проверки JS:
Заголовок: {title_result} (ожидалось: 'New Text')
Кнопка регистрации: {button_result} (ожидалось: 'Registration')
"""

    # Выводим результат в новый файл
    with open("playwright_js_result.txt", "w", encoding="utf-8") as f:
        f.write(result_text)

    print(result_text)

    page.wait_for_timeout(5000)
    browser.close()