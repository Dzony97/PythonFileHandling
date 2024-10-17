from .fake_cars_repository import fake_cars_service, fake_empty_cars_service
from ..fake_objects import mazda_car


def test_filter_data_by_mileage_various_mileage(fake_cars_service):
    excepted_result = fake_cars_service.filter_data_by_mileage(1000)
    assert excepted_result == list(filter(lambda car: car.has_mileage_greater_than(1000), excepted_result))


def test_filter_data_by_empty_list(fake_empty_cars_service):
    excepted_result = []
    assert excepted_result == fake_empty_cars_service.filter_data_by_mileage(10)


def test_filter_data_by_mileage_exact_boundary(fake_cars_service):
    excepted_result = [mazda_car]
    assert excepted_result == fake_cars_service.filter_data_by_mileage(1500)


def test_filter_data_by_mileage_all_below(fake_cars_service):
    result = fake_cars_service.filter_data_by_mileage(2600)
    assert [] == result
