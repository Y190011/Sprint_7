import requests
import allure
from config import BASE_URL, COURIER_URL
import helper

class CourierMethods:

    def create_new_courier(self,params):
        response = requests.post(f'{BASE_URL}{COURIER_URL}', data=params)
        return response.status_code, response.json()

    def login_existing_courier(self,params):
        response = requests.post(f'{BASE_URL}{COURIER_URL}/login', data=params)
        return response.status_code, response.json()

    def delete_courier_by_id(self, id):
        response = requests.delete(f'{BASE_URL}{COURIER_URL}/{id}')
        return response.status_code, response.json()


    @allure.step('Создание нового курьера, проверка и получение id')
    def creation_courier_with_verification(self): #,login, password, first_name):
        login, password, first_name = helper.create_random_courier_data()
        status_code, json_reply = self.create_new_courier({"login":login, "password":password,"first_name":first_name})
        assert status_code == 201
        assert json_reply['ok'] == True
        status_code, json_reply = self.login_existing_courier({"login":login, "password":password})
        assert status_code == 200
        assert json_reply['id'] is not None
        courier_id = json_reply['id']
        return courier_id, login, password, first_name

    @allure.step('Повторное создание курьера с уже использованными данными')
    def create_courier_again(self, login, password, first_name):
        status_code,result_json = self.create_new_courier({"login":login,"password":password,"first_name":first_name})
        assert status_code == 409
        assert result_json['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.step('Попытка создания курьера без login')
    def create_courier_without_login(self, password, first_name):
        status_code,result_json = self.create_new_courier({"password":password,"first_name":first_name})
        assert status_code == 400
        assert result_json['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.step('Попытка создания курьера без password')
    def create_courier_without_password(self, login, first_name):
        status_code, result_json = self.create_new_courier({"login": login, "first_name": first_name})
        assert status_code == 400
        assert result_json['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.step('Попытка создания курьера без first_name')
    def create_courier_without_first_name(self, login, password):
        status_code, result_json = self.create_new_courier({"login": login, "password": password})
        assert status_code == 201
        assert result_json['ok'] == True


    @allure.step('Попытка создания курьера с пустым login')
    def create_courier_with_empty_login(self, login, password, first_name):
        status_code, result_json=self.create_new_courier({"login":login, "password":password,"first_name":first_name})
        assert status_code == 400
        assert result_json['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.step('Попытка создания курьера с пустым password')
    def create_courier_with_empty_password(self, login, password, first_name):
        status_code, result_json = self.create_new_courier(
            {"login": login, "password": password, "first_name": first_name})
        assert status_code == 400
        assert result_json['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.step('Попытка создания курьера с пустым first_name')
    def create_courier_with_empty_first_name(self, login, password, first_name):
        status_code, result_json = self.create_new_courier(
            {"login": login, "password": password, "first_name": first_name})
        assert status_code == 201
        assert result_json['ok'] == True
        self.delete_courier_by_login(login, password)


    @allure.step('Попытка авторизации курьера с пустым login')
    def login_courier_without_login_field(self, password):
        status_code, result_json = self.login_existing_courier(
            {"login": "", "password": password})
        print('login', status_code, result_json)
        assert status_code == 400
        assert result_json['message'] == 'Недостаточно данных для входа'

    @allure.step('Попытка авторизации курьера с пустым password')
    def login_courier_without_password_field(self, login):
        status_code, result_json = self.login_existing_courier(
            {"login": login, "password": ""})
        assert status_code == 400
        assert result_json['message'] == 'Недостаточно данных для входа'


    @allure.step('Попытка авторизации курьера с некорректным login')
    def login_courier_with_incorrect_login_field(self, login, password):
        status_code, result_json = self.login_existing_courier({"login": login, "password": password})
        assert status_code == 404
        assert result_json['message'] == 'Учетная запись не найдена'

    @allure.step('Попытка авторизации курьера с некорретным password')
    def login_courier_with_incorrect_password_field(self, login, password):
        status_code, result_json = self.login_existing_courier({"login": login, "password": password})
        assert status_code == 404
        assert result_json['message'] == 'Учетная запись не найдена'


    def delete_courier_by_login(self, login, password):
        status_code, json_reply = self.login_existing_courier({"login":login, "password":password})
        assert status_code == 200
        assert json_reply['id'] is not None
        courier_id = json_reply['id']
        response = requests.delete(f'{BASE_URL}{COURIER_URL}/{courier_id}')
        assert response.status_code == 200


