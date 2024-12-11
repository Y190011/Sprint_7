import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods   import OrderMethods
import config
import allure

@allure.title("Тесты на проверку создания заказов и получения списка заказов")
class TestOrders:
    @allure.step("Тест - создание, чтение и прием заказов курьерами")
    @pytest.mark.parametrize('order_data', [config.ORDER_DATA_1, config.ORDER_DATA_2, config.ORDER_DATA_3])
    def test_create_order(self, courier_id, order_data):
        order_methods = OrderMethods()
        order_methods.create_and_accept_order(courier_id, order_data)

    @allure.step("Тест - создание заказов, прием заказов курьером, получение списка заказов для курьера")
    def test_order_list(self, courier_id):
        print('courier=', courier_id)
        order_methods = OrderMethods()
        order_methods.create_and_accept_order(courier_id, config.ORDER_DATA_1)
        order_methods.create_and_accept_order(courier_id, config.ORDER_DATA_2)
        order_methods.create_and_accept_order(courier_id, config.ORDER_DATA_3)
        order_list    = order_methods.get_order_list(courier_id)['orders']
        assert len(order_list) > 1







