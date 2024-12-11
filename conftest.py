import pytest
from  methods.courier_methods import CourierMethods


@pytest.fixture()
def courier_id():
    courier_methods = CourierMethods()
    courier_id = courier_methods.creation_courier_with_verification()[0]
    yield courier_id
    courier_methods.delete_courier_by_id(courier_id)

@pytest.fixture()
def courier():
    courier_methods = CourierMethods()
    courier_data = courier_methods.creation_courier_with_verification()
    yield courier_data
    courier_methods.delete_courier_by_id(courier_data[0])