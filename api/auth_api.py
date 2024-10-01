# api/auth_api.py
import requests
from test_data import REGISTER_URL, LOGIN_URL, LOGOUT_URL, REFRESH_TOKEN_URL, USER_URL


class AuthAPI:
    def __init__(self):
        self.timeout = 10

    def register(self, email=None, password=None, name=None):
        data = {
            "email": email,
            "password": password,
            "name": name
        }
        assert isinstance(REGISTER_URL, object)
        response = requests.post(REGISTER_URL, json=data)
        return response

    def login(self, email, password):
        data = {"email": email, "password": password}
        return requests.post(LOGIN_URL, json=data)

    def logout(self, refresh_token):
        data = {"token": refresh_token}
        return requests.post(LOGOUT_URL, json=data)

    def refresh_token(self, refresh_token):
        data = {"token": refresh_token}
        return requests.post(REFRESH_TOKEN_URL, json=data)

    def delete_user(self, token):
        headers = {"Authorization": token}
        response = requests.delete(USER_URL, headers=headers)
        return response
