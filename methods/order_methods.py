import allure
import requests
from data import CREATE_ORDER_URL


class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(headers=None, order_data=None):
        response = requests.post(CREATE_ORDER_URL, json=order_data, headers=headers)
        response_json = response.json()
        return response, response_json
