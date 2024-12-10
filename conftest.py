import pytest
import requests
from data import REGISTER_USER_URL, LOGIN_USER_URL, USER_DATA
from methods.user_methods import UserMethods


@pytest.fixture
def register_and_delete_user(request):
    """Фикстура для создания пользователя и его удаления после теста.
    Возвращает данные пользователя и токен."""
    name, email, password = UserMethods.register_new_user_and_return_email_password()
    user_data = {"name": name, "email": email, "password": password}

    # Регистрируем пользователя
    response = requests.post(REGISTER_USER_URL, json=user_data)
    assert response.status_code == 200

    response_json = response.json()
    access_token = response_json["accessToken"]
    assert "accessToken" in response_json

    # Возвращаем данные пользователя и токен
    yield user_data, access_token, response

    # Удаление пользователя после выполнения теста
    if "delete_user" in request.node.keywords:
        UserMethods.delete_user(access_token, user_data)

@pytest.fixture
def user_auth_token():
    """Фикстура для авторизации пользователя и получения токена"""
    response = requests.post(LOGIN_USER_URL, json={
        "email": USER_DATA["email"],
        "password": USER_DATA["password"]
    })

    response_json = response.json()
    assert "accessToken" in response_json

    return {
        "response": response,
        "accessToken": response_json["accessToken"],
    }
