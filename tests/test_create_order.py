import allure


class TestCreateOrder:

    @allure.title('Создать заказ самоката черного или серого цвета')
    def test_create_order_with_color_black_or_grey(self, create_order_with_color_black_or_grey):
        assert create_order_with_color_black_or_grey.status_code == 201

    @allure.title('Создать заказ самоката черного и серого цвета')
    def test_create_order_with_color_black_and_grey(self, create_order_with_color_black_and_grey):
        assert create_order_with_color_black_and_grey.status_code == 201

    @allure.title('Создать заказ самоката без цвета')
    def test_create_order_without_color(self, create_order_without_color):
        assert create_order_without_color.status_code == 201

    @allure.title('Создать заказ и получить номер заказа')
    def test_create_order_return_code_track_order(self, create_order_with_color_black_or_grey):
        assert 'track' in create_order_with_color_black_or_grey.json()
