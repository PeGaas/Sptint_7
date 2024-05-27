import allure


class TestAcceptOrder:

    @allure.title('Принять заказ без id курьера')
    def test_accept_order_without_courier_id_return_message_conflict(self, create_order_without_courier_id):
        assert create_order_without_courier_id.status_code == 400 and create_order_without_courier_id.json() == {
            'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title('Принять заказ с не корректным id курьера')
    def test_accept_order_with_incorrect_courier_id_return_message_not_found(self,
                                                                             create_order_with_incorrect_courier_id):
        assert create_order_with_incorrect_courier_id.status_code == 404 and create_order_with_incorrect_courier_id.json() == {
            'code': 404, 'message': 'Курьера с таким id не существует'}

    @allure.title('Принять заказ с не корректным id заказа')
    def test_accept_order_with_incorrect_order_id_return_message_error(self, create_order_with_incorrect_order_id):
        assert create_order_with_incorrect_order_id.status_code == 404 and create_order_with_incorrect_order_id.json() == {
            'code': 404, 'message': 'Заказа с таким id не существует'}
