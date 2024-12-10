import allure
import requests
from data import GET_ORDER_URL, VALID_INGREDIENTS
from methods.order_methods import OrderMethods


@allure.suite("Тесты получения заказов конкретного пользователя")
class TestGetOrder:
    @allure.title("Тест на получение заказов авторизованного пользователя")
    @allure.description("Тест удачного получения списка заказов с авторизацией")
    def test_get_orders_with_auth(self, user_auth_token):
        headers = {"Authorization": user_auth_token["accessToken"]}
        order_data = {"ingredients": VALID_INGREDIENTS}
        response_create_order, response_create_json = OrderMethods.create_order(headers=headers, order_data=order_data)
        created_order_number = response_create_json["order"]["number"]
        response_get_order = requests.get(GET_ORDER_URL, headers=headers)
        orders = response_get_order.json()["orders"]
        assert response_get_order.status_code == 200 and any(order["number"] == created_order_number for order in orders)

    @allure.title("Тест на получение заказов без авторизации")
    @allure.description("Тест на получении ошибки при получении заказа без авторизации")
    def test_get_orders_without_auth(self):
        """Тест на получение заказов без авторизации"""
        response_get_order = requests.get(GET_ORDER_URL)
        response_json = response_get_order.json()
        assert response_get_order.status_code == 401 and response_json["message"] == "You should be authorised"
