import allure
import requests
from data import CHANGE_USER_URL
from methods.user_methods import UserMethods


@allure.suite("Тесты изменение данных пользователя")
class TestChangeUser:
    @allure.title("Успешное изменение данных пользователя с авторизацией")
    @allure.description("Тест на успешное изменение имени и email авторизованного пользователя")
    def test_change_user_success(self, register_and_delete_user):
        user_data, access_token, _ = register_and_delete_user
        headers = {"Authorization": access_token}
        change_data = {
            "email": f"{UserMethods.generate_random_string(10)}@example.com",
            "name": UserMethods.generate_random_string(8)
        }
        change_response = requests.patch(CHANGE_USER_URL, json=change_data, headers=headers)
        response_json = change_response.json()
        assert change_response.status_code == 200 and response_json["user"]["name"] == change_data["name"] and response_json["user"]["email"] == change_data["email"]

    @allure.title("Изменение данных пользователя без авторизации")
    @allure.description("Тест на изменение данных пользователя без авторизации")
    def test_update_user_without_authorization(self):
        # Новые данные для обновления
        change_data = {
            "name": "UnauthorizedUser",
            "email": "unauthorizeduser@example.com"
        }
        change_response = requests.patch(CHANGE_USER_URL, json=change_data)
        response_json = change_response.json()
        assert change_response.status_code == 401 and response_json["message"] == "You should be authorised"
