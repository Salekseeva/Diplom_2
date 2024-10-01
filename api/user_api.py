# api/user_api.py
import requests
from test_data import BASE_URL


class UserAPI:
    def __init__(self):
        self.base_url = f"{BASE_URL}/api/auth/user"

    def get_user(self, token):
        headers = {"Authorization": token}
        return requests.get(self.base_url, headers=headers)

    def update_user(self, token, user_data):
        headers = {
            'Authorization': f'{token}',  # Передаем токен без "Bearer"
            'Content-Type': 'application/json'
        }
        response = requests.patch(self.base_url, json=user_data, headers=headers)
        return response

    def delete_user(self, token):
        headers = {"Authorization": token}
        return requests.delete(self.base_url, headers=headers)
