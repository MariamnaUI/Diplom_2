import allure
import requests
from data import LOGIN_USER_URL


@allure.suite("Тесты логина пользователя в систему")
class TestLoginUser:
    @allure.title("Вход с корректными данными")
    @allure.description("Тест на успешный логин")
    def test_login_user_success(self, user_auth_token):
        response = user_auth_token["response"]
        access_token = user_auth_token["accessToken"]
        assert response.status_code == 200 and access_token.startswith("Bearer ")

    @allure.title("Вход с неверными данными")
    @allure.description("Тест на логин с неверным email и паролем")
    def test_login_user_without_required_fields(self):
        login_data = {
            "email": "msh11f@mnhmjk.ru",
            "password": "wrongpassword"
        }
        response = requests.post(LOGIN_USER_URL, json=login_data)
        response_json = response.json()

        assert response.status_code == 401 and response_json["message"] == "email or password are incorrect"
