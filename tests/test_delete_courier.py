import allure


class TestDeleteCourier:

    @allure.title('Удалить курьера с не существующим id')
    def test_delete_courier_not_exist_id_return_message_error(self, delete_courier_with_not_exist_id):
        assert delete_courier_with_not_exist_id.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}

    @allure.title('Удалить курьера')
    def test_delete_courier_return_ok_true(self, delete_courier):
        assert delete_courier.json() == {'ok': True}

    @allure.title('Удалить курьера без id курьера')
    def test_delete_courier_without_id_return_message_not_found(self, delete_courier_without_id):
        assert delete_courier_without_id.json() == {'code': 404, 'message': 'Not Found.'}
