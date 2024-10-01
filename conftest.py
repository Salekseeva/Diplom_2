# conftest.py
import pytest
from api.auth_api import AuthAPI
from test_data import VALID_USER, INGREDIENTS_URL
import requests
import random

@pytest.fixture(scope="function")
def register_user():
    auth_api = AuthAPI()
    user_data = VALID_USER.copy()
    email = f"test-{random.randint(0, 10000)}@example.com"
    response = auth_api.register(email, user_data['password'], user_data['name'])
    token = response.json().get('accessToken')
    yield {"email": email, "accessToken": token}
    auth_api.delete_user(token)     # Удаление пользователя после теста


@pytest.fixture(scope="session")
def ingredients():
    """Фикстура запрашивает ингредиенты один раз перед всеми тестами"""
    response = requests.get(INGREDIENTS_URL)
    assert response.status_code == 200, "Не удалось получить ингредиенты"
    return response.json()['data']


@pytest.fixture(scope="session", autouse=True)
def cleanup():
    """Очистка после завершения всех тестов"""
    yield
    print("Все тесты завершены. Выполняем очистку.")
