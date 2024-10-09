# api/order_api.py
import requests
from test_data import ORDER_URL, INGREDIENTS_URL


class OrderAPI:
    def __init__(self):
        self.base_url = ORDER_URL
        self.ingredients_url = INGREDIENTS_URL

    def get_ingredients(self):
        response = requests.get(self.ingredients_url)
        return response.json()

    def create_order(self, token, ingredients):
        headers = {"Authorization": token, "Content-Type": "application/json"} if token else {"Content-Type": "application/json"}
        data = {"ingredients": ingredients}
        return requests.post(self.base_url, json=data, headers=headers)

    def get_user_orders(self, token):
        headers = {"Authorization": token}
        return requests.get(self.base_url, headers=headers)
