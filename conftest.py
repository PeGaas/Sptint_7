import pytest
import requests

from data_generator import generate_login, generate_password, generate_first_name, generate_metro_station, \
    generate_phone, generate_address, generate_delivery_date, generate_rent_time, generate_comment, generate_color, \
    generate_limit_orders, generate_courier_id
from data_static import MAIN_URL

login = generate_login()
password = generate_password()
first_name = generate_first_name()
limit_orders = generate_limit_orders()
courier_id = generate_courier_id()


@pytest.fixture()
def create_new_courier():
    # Создать нового курьера
    payload = {"login": login, "password": password, "firstName": first_name}
    response = requests.post(f'{MAIN_URL}/api/v1/courier', data=payload)
    print(response.json())
    yield response
    # Получить id курьера
    payload = {"login": login, "password": password}
    response = requests.post(f'{MAIN_URL}/api/v1/courier/login', data=payload)
    id_courier = response.json()['id']

    # Удалить курьера, который был создан
    requests.delete(f'{MAIN_URL}/api/v1/courier/{id_courier}')


@pytest.fixture()
def create_new_courier_without_required_field():
    # Создать нового курьера без логина или пароля
    payload = {"login": login, "firstName": first_name}
    response = requests.post(f'{MAIN_URL}/api/v1/courier', data=payload)
    yield response


@pytest.fixture()
def create_order_with_color_black_or_grey():
    # Создать заказ самоката с ЧЕРНЫМ или СЕРЫМ цветом
    payload_order = {"firstName": generate_first_name(), "lastName": generate_password(), "address": generate_address(),
                     "metroStation": generate_metro_station(), "phone": generate_phone(),
                     "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                     "comment": generate_comment(),
                     "color": generate_color()}
    response = requests.post(f'{MAIN_URL}/api/v1/orders', json=payload_order)
    yield response


@pytest.fixture()
def create_order_with_color_black_and_grey():
    # Создать заказ самоката с ЧЕРНЫМ и СЕРЫМ цветом
    payload_order = {"firstName": generate_first_name(), "lastName": generate_password(), "address": generate_address(),
                     "metroStation": generate_metro_station(), "phone": generate_phone(),
                     "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                     "comment": generate_comment(),
                     "color": ['BLACK', 'GREY']}
    response = requests.post(f'{MAIN_URL}/api/v1/orders', json=payload_order)
    yield response


@pytest.fixture()
def create_order_without_color():
    # Создать заказ самоката без указания цвета
    payload_order = {"firstName": generate_first_name(), "lastName": generate_password(), "address": generate_address(),
                     "metroStation": generate_metro_station(), "phone": generate_phone(),
                     "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                     "comment": generate_comment(),
                     "color": ['']}
    response = requests.post(f'{MAIN_URL}/api/v1/orders', json=payload_order)
    yield response


@pytest.fixture()
def get_orders():
    # Получить список заказов
    params = {"limit": limit_orders}
    response = requests.get(f'{MAIN_URL}/api/v1/orders', params=params)
    yield response


@pytest.fixture()
def delete_courier():
    # Создать нового курьера
    payload = {"login": login, "password": password, "firstName": first_name}
    response = requests.post(f'{MAIN_URL}/api/v1/courier', data=payload)
    yield response
    # Получить id курьера
    payload = {"login": login, "password": password}
    response = requests.post(f'{MAIN_URL}/api/v1/courier/login', data=payload)
    id_courier = response.json()['id']

    # Удалить курьера, который был создан
    requests.delete(f'{MAIN_URL}/api/v1/courier/{id_courier}')


@pytest.fixture()
def delete_courier_with_not_exist_id():
    payload = {"login": login, "password": password}
    response = requests.delete(f'{MAIN_URL}/api/v1/courier/{courier_id}')
    yield response


@pytest.fixture()
def delete_courier_without_id():
    response = requests.delete(f'{MAIN_URL}/api/v1/courier')
    yield response


@pytest.fixture()
def create_order_without_courier_id():
    # Создать заказ
    payload_order = {"firstName": generate_first_name(), "lastName": generate_password(), "address": generate_address(),
                     "metroStation": generate_metro_station(), "phone": generate_phone(),
                     "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                     "comment": generate_comment(),
                     "color": generate_color()}
    response_order = requests.post(f'{MAIN_URL}/api/v1/orders', json=payload_order)
    order_id = response_order.json()['track']

    # Создать курьера
    payload_courier = {"login": login, "password": password, "firstName": first_name}
    requests.post(f'{MAIN_URL}/api/v1/courier', data=payload_courier)

    # Принять заказ
    params = {'courierId': ""}
    response = requests.put(f'{MAIN_URL}/api/v1/orders/accept/{order_id}', params=params)
    yield response


@pytest.fixture()
def create_order_with_incorrect_courier_id():
    # Создать заказ
    payload_order = {"firstName": generate_first_name(), "lastName": generate_password(), "address": generate_address(),
                     "metroStation": generate_metro_station(), "phone": generate_phone(),
                     "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                     "comment": generate_comment(),
                     "color": generate_color()}
    response_order = requests.post(f'{MAIN_URL}/api/v1/orders', json=payload_order)
    order_id = response_order.json()['track']

    # Принять заказ
    params = {'courierId': generate_courier_id()}
    response = requests.put(f'{MAIN_URL}/api/v1/orders/accept/{order_id}', params=params)
    yield response


@pytest.fixture()
def create_order_with_incorrect_order_id():
    # Создать курьера
    payload_courier = {"login": login, "password": password, "firstName": first_name}
    requests.post(f'{MAIN_URL}/api/v1/courier', data=payload_courier)
    response_courier = requests.post(f'{MAIN_URL}/api/v1/courier/login', data=payload_courier)
    id_courier = response_courier.json()['id']

    # Принять заказ
    params = {'courierId': id_courier}
    response = requests.put(f'{MAIN_URL}/api/v1/orders/accept/{id_courier}', params=params)
    yield response


@pytest.fixture()
def get_order_by_id():
    # Создать заказ самоката с ЧЕРНЫМ или СЕРЫМ цветом
    payload_order = {"firstName": generate_first_name(), "lastName": generate_password(), "address": generate_address(),
                     "metroStation": generate_metro_station(), "phone": generate_phone(),
                     "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                     "comment": generate_comment(),
                     "color": generate_color()}
    response = requests.post(f'{MAIN_URL}/api/v1/orders', json=payload_order)
    order_id = response.json()['track']

    params = {"t": order_id}
    response = requests.get(f'{MAIN_URL}/api/v1/orders/track', params=params)
    yield response


@pytest.fixture()
def get_order_without_id():
    # Создать заказ самоката с ЧЕРНЫМ или СЕРЫМ цветом
    payload_order = {"firstName": generate_first_name(), "lastName": generate_password(), "address": generate_address(),
                     "metroStation": generate_metro_station(), "phone": generate_phone(),
                     "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                     "comment": generate_comment(),
                     "color": generate_color()}
    response = requests.post(f'{MAIN_URL}/api/v1/orders', json=payload_order)

    params = {"t": ""}
    response = requests.get(f'{MAIN_URL}/api/v1/orders/track', params=params)
    yield response


@pytest.fixture()
def get_order_by_not_exist_id():
    # Создать заказ самоката с ЧЕРНЫМ или СЕРЫМ цветом
    payload_order = {"firstName": generate_first_name(), "lastName": generate_password(), "address": generate_address(),
                     "metroStation": generate_metro_station(), "phone": generate_phone(),
                     "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                     "comment": generate_comment(),
                     "color": generate_color()}
    response = requests.post(f'{MAIN_URL}/api/v1/orders', json=payload_order)

    params = {"t": 111111111}
    response = requests.get(f'{MAIN_URL}/api/v1/orders/track', params=params)
    yield response
