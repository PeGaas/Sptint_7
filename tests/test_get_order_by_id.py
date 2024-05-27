import allure


class TestGetOrderById:

    @allure.title('Получить заказ по его id')
    def test_get_order_by_id_true(self, get_order_by_id):
        assert 'order' in get_order_by_id.json()

    @allure.title('Получить заказ без его id')
    def test_get_order_without_id_return_bad_request(self, get_order_without_id):
        assert get_order_without_id.status_code == 400 and get_order_without_id.json() == {'code': 400,
                                                                                           'message': 'Недостаточно данных для поиска'}

    @allure.title('Получить заказ id, которого не существует')
    def test_get_order_by_not_exist_id_return_not_found(self, get_order_by_not_exist_id):
        assert get_order_by_not_exist_id.status_code == 404 and get_order_by_not_exist_id.json() == {'code': 404, 'message': 'Заказ не найден'}
