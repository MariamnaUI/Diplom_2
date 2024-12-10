import allure
import pytest
import requests
from data import REGISTER_USER_URL, USER_DATA


@allure.suite("Тесты создания пользователя")
@pytest.mark.delete_user
class TestRegisterUser:
    @allure.title("Создание нового пользователя")
    @allure.description("Тест успешного создания нового пользователя")
    def test_register_user_success(self, register_and_delete_user):
        user_data, access_token, response = register_and_delete_user
        assert response.status_code == 200 and "Bearer " in access_token

    @allure.title("Создание пользователя, который уже зарегистрирован")
    @allure.description("Тест создания пользователя с уже существующим email")
    def test_register_duplicate_user(self, register_and_delete_user):
        existing_user_data, _, _ = register_and_delete_user
        response = requests.post(REGISTER_USER_URL, json=existing_user_data)
        response_json = response.json()
        assert response.status_code == 403 and response_json["success"] is False

    @allure.title("Создание пользователя без обязательного поля")
    @allure.description("Тест создания пользователя без указания обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_register_user_without_required_fields(self, missing_field):
        del USER_DATA[missing_field]
        response = requests.post(REGISTER_USER_URL, json=USER_DATA)
        response_json = response.json()
        assert response.status_code == 403 and response_json["message"] == "Email, password and name are required fields"
