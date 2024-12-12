# Здесь храним данные
BASE_URL    = 'https://qa-scooter.praktikum-services.ru/api/v1/'
ORDER_URL   = 'orders/'
COURIER_URL = 'courier/'


ORDER_DATA_1 = {"firstname":"Николай", "lastname":"Николаев","address":"ул. Ленина 11", "metroStation":"Черкизовская",
                "phone":"89999999999", "rentTime":"2", "deliveryDate":"2024-12-12", "comment":"позвонить",
                "color":"BLACK"}
ORDER_DATA_2 = {"firstname":"Петр", "lastname":"Петров","address":"ул. Кирова 13", "metroStation":"Сокольники",
                "phone":"87777777777", "rentTime":"3", "deliveryDate":"2024-12-13", "comment":"написать",
                "color":"GRAY"}
ORDER_DATA_3 = {"firstname":"Сидор", "lastname":"Сидоров","address":"ул. Панина 15", "metroStation":"Волжская",
                "phone":"85555555555", "rentTime":"1", "deliveryDate":"2024-12-15", "comment":"сообщить",
                "color":["BLACK", "GRAY"]}


LOGIN_IS_ALREADY_IN_USE           = 'Этот логин уже используется. Попробуйте другой.'
NOT_ENOUGH_DATA_TO_CREATE_ACCOUNT = 'Недостаточно данных для создания учетной записи'
NOT_ENOUGH_DATA_TO_LOGIN          = 'Недостаточно данных для входа'
ACCOUNT_NOT_FOUND                 = 'Учетная запись не найдена'
