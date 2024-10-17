import pytest
from .fake_cars_repository import fake_cars_service, fake_empty_cars_service
from ..fake_objects import bmw_car, audi_car, mazda_car


@pytest.mark.parametrize('attribute,min_range,max_range,expected', [("price", 100, 201, [audi_car, mazda_car]),
                                                                    ("price", 140, 260, [mazda_car]),
                                                                    ("mileage", 1499, 2500, [audi_car]),
                                                                    ("mileage", 1500, 2500, [])])
def test_cars_in_range_by_number_values(fake_cars_service, attribute, min_range, max_range, expected):
    assert fake_cars_service.cars_in_range(attribute, min_range, max_range) == expected


def test_cars_with_empty_data(fake_empty_cars_service):
    assert fake_empty_cars_service.cars_in_range('price', 100, 101) == []