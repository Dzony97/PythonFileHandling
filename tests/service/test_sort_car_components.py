from .fake_cars_repository import fake_cars_service, fake_empty_cars_service
from ..fake_objects import mazda_car, bmw_car, audi_car


def test_sort_car_components(fake_cars_service):
    excepted_result = [audi_car, bmw_car, mazda_car]
    assert excepted_result == fake_cars_service.sort_car_components()


def test_sort_car_components_without_components(fake_cars_service):
    excepted_result = [audi_car, bmw_car, mazda_car, mazda_car]
    fake_cars_service.car_repository._cars.append(mazda_car)
    assert excepted_result == fake_cars_service.sort_car_components()


def test_sort_car_components_by_empty_data(fake_empty_cars_service):
    excepted_result = []
    assert excepted_result == fake_empty_cars_service.sort_car_components()
