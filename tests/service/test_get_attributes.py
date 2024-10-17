import pytest
from .fake_cars_repository import fake_cars_service


def test_when_attribute_is_not_correct(fake_cars_service):
    with pytest.raises(ValueError) as err:
        cars = fake_cars_service()
        cars.get_attributes('test')
    assert 'Invalid attribute' == str(err.value)


def test_when_attribute_is_correct(fake_cars_service):
    cars = fake_cars_service()
    assert cars.get_attributes('model') == ['AUDI', 'BMW', 'MAZDA']