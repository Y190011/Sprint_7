import requests
from config import BASE_URL, ORDER_URL
import json
import allure

class OrderMethods:

    @allure.title("Создание заказа")
    def post_order(self, order_data):
        json_string  = json.dumps(order_data)
        response = requests.post(f'{BASE_URL}{ORDER_URL}', data = json_string)
        assert response.status_code == 201
        assert response.json()['track'] is not None
        return response.json()['track']


    @allure.title("Чтение заказа")
    def get_order(self, order_track):
        response = requests.get(f'{BASE_URL}{ORDER_URL}track?t={order_track}')
        assert response.status_code == 200
        return response.json()['order']['id']

    @allure.title("Прием заказа курьером")
    def accept_order(self, courier_id, order_track):
        response = requests.put(f'{BASE_URL}{ORDER_URL}accept/{order_track}?courierId={courier_id}')
        assert response.status_code == 200
        assert response.json()['ok'] == True

    @allure.title("Тест на создание, чтение и прием заказа курьером")
    def create_and_accept_order(self, courier_id, order_data):
        print('order_data', order_data)
        track = self.post_order(order_data)
        order_id = self.get_order(track)
        self.accept_order(courier_id, order_id)
        return order_id

    @allure.title("Получение списка заказов для курьера")
    def get_order_list(self, courier_id):
        response = requests.get(f"{BASE_URL}orders?courierId={courier_id}")
        return response.json()