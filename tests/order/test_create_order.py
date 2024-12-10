import allure
import requests
from data import VALID_INGREDIENTS, CREATE_ORDER_URL, INVALID_INGREDIENTS
from methods.order_methods import OrderMethods


@allure.suite("Тесты создания заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией")
    @allure.description("Тест на создание заказа с авторизацией с корректными ингредиентами")
    def test_create_order_with_auth(self, user_auth_token):
        headers = {"Authorization": user_auth_token["accessToken"]}
        order_data = {"ingredients": VALID_INGREDIENTS}
        response, response_json = OrderMethods.create_order(headers=headers, order_data=order_data)
        assert response.status_code == 200 and response_json["success"] is True

    @allure.title("Создание заказа без авторизации")
    @allure.description("Тест на создание заказа без авторизации")
    def test_create_order_without_auth(self):
        """Тест на создание заказа без авторизации"""
        order_data = {"ingredients": VALID_INGREDIENTS}
        response, response_json = OrderMethods.create_order(order_data=order_data)
        assert response.status_code == 401

    @allure.title("Создание заказа с валидными ингредиентами")
    @allure.description("Тест на создание заказа с валидными ингредиентами")
    def test_create_order_with_ingredients(self, user_auth_token):
        headers = {"Authorization": user_auth_token["accessToken"]}
        order_data = {"ingredients": VALID_INGREDIENTS}
        response, response_json = OrderMethods.create_order(headers=headers, order_data=order_data)
        assert response.status_code == 200 and response_json["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Тест на создание заказа без указания ингредиентов")
    def test_create_order_without_ingredients(self, user_auth_token):
        headers = {"Authorization": user_auth_token["accessToken"]}
        order_data = {"ingredients": []}
        response, response_json = OrderMethods.create_order(headers=headers, order_data=order_data)
        assert response.status_code == 400 and response_json["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с невалидными ингредиентами")
    @allure.description("Тест на создание заказа с невалидными хешами ингредиентов")
    def test_create_order_with_invalid_ingredients(self, user_auth_token):
        headers = {"Authorization": user_auth_token["accessToken"]}
        order_data = {"ingredients": INVALID_INGREDIENTS}
        response = requests.post(CREATE_ORDER_URL, json=order_data, headers=headers)
        assert response.status_code == 500
