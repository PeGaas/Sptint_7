import allure
from conftest import limit_orders


class TestListOrders:

    @allure.title('Получить заказы и проверить тело ответа возвращает список заказов')
    def test_get_orders_return_list_orders(self, get_orders):
        assert len(get_orders.json()['orders']) == limit_orders
