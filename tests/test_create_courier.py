import allure
import requests
from conftest import login, password, first_name
from data_generator import generate_password, generate_first_name
from data_static import MAIN_URL


class TestCreateCourier:

    @allure.title('Создать двух одинаковых курьеров')
    def test_create_two_same_courier_show_message_conflict(self, create_new_courier):
        # Создать еще одного такого же курьера
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(f'{MAIN_URL}/api/v1/courier', data=payload)

        assert response.status_code == 409 and response.json() == {"code": 409,
                                                                   "message": "Этот логин уже используется. Попробуйте другой."}

    @allure.title('Создать курьера и получить статус код 201')
    def test_create_courier_return_status_code_201(self, create_new_courier):
        assert create_new_courier.status_code == 201

    @allure.title('Создать курьера и получить ответ от сервера ok: True')
    def test_create_courier_return_message_ok_true(self, create_new_courier):
        assert create_new_courier.json() == {"ok": True}

    @allure.title('Создать курьера без логина или пароля')
    def test_create_courier_without_required_field_show_message_bad_request(self,
                                                                            create_new_courier_without_required_field):
        assert create_new_courier_without_required_field.json() == {'code': 400,
                                                                    'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Создать курьера c логином, который уже существует в системе')
    def test_create_courier_with_login_already_exists_show_message_conflict(self, create_new_courier):
        # Создать еще одного курьера с таким же логином
        payload = {"login": login, "password": generate_password(), "firstName": generate_first_name()}
        response = requests.post(f'{MAIN_URL}/api/v1/courier', data=payload)

        assert response.status_code == 409 and response.json() == {"code": 409,
                                                                   "message": "Этот логин уже используется. Попробуйте другой."}
