# Анализ кода playwright_events.py

## Общая структура

Файл демонстрирует работу с событиями (events) в Playwright — подписку на запросы и ответы при навигации страницы.

## Активный код

### 1. Импорты (строка 1)
```python
from playwright.sync_api import sync_playwright, Request, Response
```
Импортируются синхронный контекстный менеджер `sync_playwright`, а также типы `Request` и `Response` для аннотации параметров.

### 2. Функции-обработчики (строки 3-7)
```python
def log_request(request: Request):
    print(f"Request: {request.url}")

def log_response(response: Response):
    print(f"Response: {response.url}")
```
Две простые функции, которые принимают объекты запроса/ответа и выводят их URL в консоль.

### 3. Основной блок (строки 9-24)
- **Строка 11**: `browser = playwright.chromium.launch(headless=False)` — открывается браузер Chromium в видимом режиме.
- **Строка 12**: `page = browser.new_page()` — создаётся новая вкладка.
- **Строки 18-19**: `page.on("request", log_request)` и `page.on("response", log_response)` — подписка на события. `page.on(...)` регистрирует обработчик, который будет вызываться каждый раз при возникновении события.
- **Строка 22**: `page.goto(...)` — переход на страницу логина. Во время загрузки срабатывают обработчики для каждого HTTP-запроса и ответа.
- **Строка 24**: `page.wait_for_timeout(5000)` — ожидание 5 секунд перед закрытием.

## Закомментированный код

### 1. Функция `log_response_body` (строки 14-16)
```python
# def log_response_body(response):
#     if response.ok:
#         print(f"Response body: {response.body()}")
```
Задумка: выводить тело ответа, но только для успешных запросов (`response.ok`). Закомментирована, вероятно, чтобы не засорять консоль большим объёмом данных.

**Важный нюанс**: вызов `response.body()` может вернуть только один раз (body — это ReadableStream, который потребляется единожды). Если нужно работать с телом, следует использовать `response.text()` или `response.json()`.

### 2. Подписка на `log_response_body` (строка 20)
```python
# page.on("response", log_response_body)
```
Планировалась вторая подписка на `response` для вывода тела ответа, но отключена вместе с функцией выше.

### 3. Динамический обработчик через лямбду (строки 27-30)
```python
# listener = lambda request: print(f"Request: {request.url}")
# page.on("request", listener)  # Добавляем обработчик
# page.remove_listener("request", listener)  # Убираем обработчик
```
Показывает альтернативный способ: лямбда-функция вместо именованной. Ключевая особенность — `remove_listener()` позволяет отписаться от события, передав ту же ссылку на функцию. Для лямбды это работает, так как ссылка сохранена в переменную `listener`.

### 4. Фильтрация событий (строки 33-36)
```python
# def log_specific_requests(request):
#     if "googleapis.com" in request.url:
#         print(f"Filtered request: {request.url}")
# page.on("request", log_specific_requests)
```
Пример фильтрации: обработчик срабатывает на все запросы, но выводит только те, что содержат `googleapis.com` в URL. Это позволяет не захламлять вывод второстепенными запросами.

## Итог

| Часть кода | Статус | Назначение |
|-----------|--------|------------|
| `log_request` / `log_response` | Активен | Вывод URL запросов и ответов |
| `log_response_body` | Закомментирован | Вывод тела успешных ответов |
| Лямбда-обработчик + `remove_listener` | Закомментирован | Динамическое управление подпиской |
| `log_specific_requests` с фильтром | Закомментирован | Фильтрация запросов по URL |
