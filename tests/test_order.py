# tests/test_order.py
import allure
from api.order_api import OrderAPI
from utils.assert_helpers import assert_response


@allure.feature("Order Creation")
class TestOrder:
    @allure.story("Создание заказа с авторизацией + с ингредиентами. Позитивный тест.")
    def test_create_order_with_auth(self, register_user, ingredients):
        order_api = OrderAPI()
        valid_ingredient_id = ingredients[0]['_id']
        response = order_api.create_order(register_user['accessToken'], ingredients=[valid_ingredient_id])
        assert_response(response, 200)

    @allure.story("Создание заказа без авторизации")
    def test_create_order_without_auth(self, ingredients):
        order_api = OrderAPI()
        valid_ingredient_id = ingredients[0]['_id']
        response = order_api.create_order(None, ingredients=[valid_ingredient_id])
        # При тестировании создания заказа без авторизации, сервер возвращает код 200 OK вместо ожидаемого кода 401 Unauthorized.
        # Это позволяет неавторизованному пользователю успешно создать заказ, что не соответствует ожидаемому поведению
        # системы безопасности.
        assert_response(response, 401, "You should be authorised")


    @allure.story("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, register_user, ingredients):
        order_api = OrderAPI()
        response = order_api.create_order(register_user['accessToken'], ingredients=[])
        assert_response(response, 400, "Ingredient ids must be provided")

    @allure.story("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredients(self, register_user):
        order_api = OrderAPI()
        invalid_ingredient_id = ""  # Используем неверный хеш ингредиента
        response = order_api.create_order(register_user['accessToken'], ingredients=[invalid_ingredient_id])
        # При отправке запроса с некорректным ID ингредиента сервер возвращает HTML-ответ вместо JSON,
        # что приводит к ошибке декодирования. Ожидается, что сервер вернет корректный JSON с ошибкой,
        # описывающей проблему с неверным ингредиентом.
        assert_response(response, 500, "Internal Server Error")

    @allure.story("Получение заказов авторизованным пользователем")
    def test_get_orders_with_auth(self, register_user):
        order_api = OrderAPI()
        response = order_api.get_user_orders(register_user['accessToken'])
        assert_response(response, 200)

    @allure.story("Получение заказов неавторизованным пользователем")
    def test_get_orders_without_auth(self):
        order_api = OrderAPI()
        response = order_api.get_user_orders(None)
        assert_response(response, 401, "You should be authorised")
