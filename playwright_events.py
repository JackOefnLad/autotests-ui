from playwright.sync_api import sync_playwright, Request, Response # type: ignore

def log_request(request: Request):
    print(f"Request: {request.url}")

def log_response(response: Response):
    print(f"Response: {response.url}")

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # def log_response_body(response):
    #     if response.ok:
    #         print(f"Response body: {response.body()}")

    page.on("request", log_request)
    page.on("response", log_response)
    # page.on("response", log_response_body)

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    page.wait_for_timeout(5000) 

# Динамический обработчик события
# listener = lambda request: print(f"Request: {request.url}")

# page.on("request", listener)  # Добавляем обработчик
# page.remove_listener("request", listener)  # Убираем обработчик

# Фильтрация событий
# def log_specific_requests(request):
#     if "googleapis.com" in request.url:
#         print(f"Filtered request: {request.url}")

# page.on("request", log_specific_requests)