import random
import string
import time
import allure
import requests
from data import DELETE_USER_URL


class UserMethods:
    @staticmethod
    @allure.step("Генерация случайной строки")
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    @allure.step("Регистрация нового пользователя")
    def register_new_user_and_return_email_password():
        name = UserMethods.generate_random_string(10)
        email = f"{UserMethods.generate_random_string(10)}@example.com"
        password = UserMethods.generate_random_string(10)
        return name, email, password

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(access_token, user_data):
        headers = {"Authorization": access_token}
        max_attempts = 3  # Максимальное количество попыток
        for attempt in range(max_attempts):
            delete_response = requests.delete(DELETE_USER_URL, headers=headers)
            if delete_response.status_code in [200, 202]:
                print(f"Пользователь успешно удалён: {user_data}")
                return
            print(f"Попытка удаления не удалась ({attempt + 1}): {delete_response.status_code}")
            time.sleep(2)  # Задержка между попытками

            # Если удаление не удалось за все попытки
        raise AssertionError(f"Не удалось удалить пользователя после {max_attempts} попыток: {user_data}")
