import pytest
from methods.courier_methods import CourierMethods
import helper
import allure


@allure.title("Тесты на проверку создания и авторизации курьеров")
class TestCreateCourier:

    @allure.step("Тест на создание курьера, авторизацию и попытку повторного создания")
    def test_create_courier(self, courier):
        courier_methods = CourierMethods()
        courier_id, login, password, first_name = courier
        courier_methods.create_courier_again(login, password, first_name)

    @allure.step("Тест на попытку создания курьера с пустым значением обязательнх полей")
    def test_create_courier_with_empty_values(self):
        courier_methods = CourierMethods()
        login, password, first_name = helper.create_random_courier_data()
        courier_methods.create_courier_with_empty_login("", password, first_name)
        courier_methods.create_courier_with_empty_password(login, "", first_name)
        courier_methods.create_courier_with_empty_first_name(login, password, "")

    @allure.step("Тест на попытку создания курьера с отсутствующими обязательными полями")
    def test_create_courier_without_some_data(self):
        courier_methods = CourierMethods()
        login, password, first_name = helper.create_random_courier_data()
        courier_methods.create_courier_without_login(password, first_name)
        courier_methods.create_courier_without_password(login, first_name)
        courier_methods.create_courier_without_first_name(login, password)

    @allure.step("Тест на попытку авторизации курьера с отсутствующими обязательными полями")
    def test_autorization_courier_without_required_fields(self, courier):
        courier_id, login, password, first_name = courier
        courier_methods = CourierMethods()
        courier_methods.login_courier_without_login_field(password)
        courier_methods.login_courier_without_password_field(login)

    @allure.step("Тест на попытку авторизации курьера с некорректными логином/паролем")
    def test_login_with_incorrect_login_data(self, courier):
        courier_id, login, password, first_name = courier
        courier_methods = CourierMethods()
        incorrect_login = login[0:7] + '+$#'
        incorrect_password = password[0:7] + '-%&'
        courier_methods.login_courier_with_incorrect_login_field(incorrect_login,password)
        courier_methods.login_courier_with_incorrect_password_field(login, incorrect_password)
