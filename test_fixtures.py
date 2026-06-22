import pytest

@pytest.fixture(autouse=True) # автоматически ДО теста
def send_analytics_data():
    print("[AUTOUSE]")

@pytest.fixture(scope="session") #один раз от начала и до конца
def settings():
    print("[SESSION]")

@pytest.fixture(scope="class") #один раз на тестовый класс
def user():
    print("[CLASS]")


@pytest.fixture(scope="function") #один раз на тестовую функцию
def browser():
    print("[FUNCTION]")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...
    def test_user_can_create_course(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self,settings, user, browser):
        ...