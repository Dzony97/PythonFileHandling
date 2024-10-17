import pytest
from .fake_cars_repository import fake_cars_service, fake_empty_cars_service


def test_sorted_data_by_price_ascending(fake_cars_service):
    excepted_result = fake_cars_service.sorted_data_ascending_or_descending('price', False)
    assert excepted_result == sorted(excepted_result, key=lambda car: car.price)


def test_sorted_data_by_price_descending(fake_cars_service):
    excepted_result = fake_cars_service.sorted_data_ascending_or_descending('price', True)
    assert excepted_result == sorted(excepted_result, key=lambda car: car.price, reverse=True)


def test_sorted_data_by_mileage_ascending(fake_cars_service):
    excepted_result = fake_cars_service.sorted_data_ascending_or_descending('mileage', False)
    assert excepted_result == sorted(excepted_result, key=lambda car: car.mileage)


def test_sorted_data_by_mileage_descending(fake_cars_service):
    excepted_result = fake_cars_service.sorted_data_ascending_or_descending('mileage', True)
    assert excepted_result == sorted(excepted_result, key=lambda car: car.mileage, reverse=True)


def test_should_raise_error_for_invalid_attribute(fake_cars_service):
    with pytest.raises(ValueError):
        fake_cars_service.sorted_data_ascending_or_descending('invalid_attribute')


def test_should_return_empty_list_for_empty_list_sorted(fake_empty_cars_service):
    assert fake_empty_cars_service.sorted_data_ascending_or_descending('price', False) == []
