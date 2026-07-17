import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number",[1,2,3, -1])
def test_numbers (number: int):
    assert number > 0

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
# В данном случае в качестве данных используется список с кортежами
def test_several_numbers(number: int, expected: int):
    # Возводим число number в квадрат и проверяем, что оно равно ожидаемому
    assert number ** 2 == expected

# Мы передаем два аргумента — number и expected — в каждый прогон теста. Это позволяет тестировать различные входные данные и ожидания в одном тесте.
# В декораторе @pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)]) указаны три набора параметров.
# Названия аргументов number и expected должны совпадать с именами параметров функции test_several_numbers.
# В квадратных скобках отображаются значения каждого набора параметров, с которыми запускался тест, что позволяет легко отследить, с какими данными работал каждый прогон.
# Пример: test_several_numbers[1-1] указывает, что тест был выполнен с number=1 и expected=1

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])  # Параметризируем по операционной системе
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])  # Параметризируем по браузеру
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0  # Проверка указана для примера


@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request: SubRequest) -> str:
    return request.param
# Это как цикл for по списку браузеров, но на уровне pytest: для каждого браузера из списка запускается полный набор тестов.

def test_open_browser(browser: str):
    # Используем фикстуру в автотесте, она вернет нам браузер в виде строки
    print(f"Running test on browser: {browser}")

# Для тестовых классов параметризация указывается для самого класса
@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        # Данный автотест будет запущен 4 раза
        print(f"User with operations: {user}")

    # Аналогично тут передается "user"
    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

# Словарь пользователей: номер телефона — ключ, описание — значение
users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}

@pytest.mark.parametrize(
    "phone_number", 
    users.keys(),  # Передаем список номеров телефонов
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"  # Генерируем идентификаторы динамически
)
def test_identifiers(phone_number: str):
    pass
