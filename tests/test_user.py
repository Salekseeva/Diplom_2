# tests/test_user.py
import allure
from api.user_api import UserAPI
from utils.assert_helpers import assert_response
from test_data import UPDATED_USER


@allure.feature("User Data")
class TestUser:
    @allure.story("Изменение данных пользователя с авторизацией")
    def test_update_user_with_auth(self, register_user):
        user_api = UserAPI()
        token = register_user['accessToken']
        response = user_api.update_user(token, UPDATED_USER)
        assert_response(response, 200)

    @allure.story("Изменение данных пользователя без авторизации")
    def test_update_user_without_auth(self):
        user_api = UserAPI()
        response = user_api.update_user(None, UPDATED_USER)
        assert_response(response, 401, "You should be authorised")
