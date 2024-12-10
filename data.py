BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'

REGISTER_USER_URL = f'{BASE_URL}auth/register'
LOGIN_USER_URL = f'{BASE_URL}auth/login'
CHANGE_USER_URL = f'{BASE_URL}auth/user'
DELETE_USER_URL = f'{BASE_URL}auth/user'

CREATE_ORDER_URL = f'{BASE_URL}orders'
GET_ORDER_URL = f'{BASE_URL}orders'

USER_DATA = {
            "email": "msh11f@mnhmjk.ru",
            "password": "124password123",
            "name": "Мари"
}

VALID_INGREDIENTS = ["61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6d"]
INVALID_INGREDIENTS = ["invalid_hash1", "invalid_hash2"]
