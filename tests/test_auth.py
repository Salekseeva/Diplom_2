# tests/test_auth.py
import allure
import pytest
from api.auth_api import AuthAPI
from test_data import VALID_USER, EXISTING_USER, INVALID_USER
from utils.assert_helpers import assert_response
from utils.helpers import generate_unique_email


@allure.feature("Authentication")
class TestAuth:
    @allure.story("Создание уникального пользователя")
    def test_create_unique_user(self):
        auth_api = AuthAPI()
        email = generate_unique_email()
        response = auth_api.register(email, VALID_USER['password'], VALID_USER['name'])
        assert_response(response, 200)

    @allure.story("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self):
        auth_api = AuthAPI()
        response = auth_api.register(EXISTING_USER['email'], EXISTING_USER['password'], EXISTING_USER['name'])
        assert_response(response, 403, "User already exists")

    @allure.story("Создание пользователя без одного из обязательных полей")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, missing_field):
        auth_api = AuthAPI()
        user_data = VALID_USER.copy()
        user_data.pop(missing_field)
        response = auth_api.register(**user_data)
        assert_response(response, 403, "Email, password and name are required fields")

    @allure.story("Логин под существующим пользователем")
    def test_login_existing_user(self):
        auth_api = AuthAPI()
        response = auth_api.login(EXISTING_USER['email'], EXISTING_USER['password'])
        assert_response(response, 200)

    @allure.story("Логин с неверным логином и паролем")
    def test_login_invalid_user(self):
        auth_api = AuthAPI()
        response = auth_api.login(INVALID_USER['email'], INVALID_USER['password'])
        assert_response(response, 401, "email or password are incorrect")
