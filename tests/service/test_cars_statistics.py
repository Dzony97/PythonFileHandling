import pytest
from .fake_cars_repository import fake_empty_cars_service, fake_cars_service


def test_cars_statistics_by_price(fake_cars_service):
    """
    Test that cars_statistics returns the correct statistics for car prices.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    expected_result = (
        f'The highest price: 260,'
        f' the lowest price: 140,'
        f' the average price: 200.0.'
    )
    assert expected_result == fake_cars_service.cars_statistics('price')


def test_cars_statistics_by_mileage(fake_cars_service):
    """
    Test that cars_statistics returns the correct statistics for car mileage.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    expected_result = (
        f'The highest mileage: 2500,'
        f' the lowest mileage: 1400,'
        f' the average mileage: 1800.0.'
    )
    assert expected_result == fake_cars_service.cars_statistics('mileage')


def test_cars_statistics_by_empty_data(fake_empty_cars_service):
    """
    Test that cars_statistics raises an error when called on an empty dataset.

    :param fake_empty_cars_service: A CarService instance with no cars.
    """
    with pytest.raises(ValueError) as err:
        fake_empty_cars_service.cars_statistics('price')
    assert 'max() iterable argument is empty' in str(err.value)
