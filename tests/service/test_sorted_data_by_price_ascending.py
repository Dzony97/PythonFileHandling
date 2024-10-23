import pytest
from .fake_cars_repository import fake_cars_service, fake_empty_cars_service


def test_sorted_data_by_price_ascending(fake_cars_service):
    """
    Test sorting car data by price in ascending order.

    This test verifies that the sorted_data_ascending_or_descending method
    returns cars sorted by price in ascending order. The expected result
    is checked against the actual output of the method.

    :param fake_cars_service: A CarService instance with predefined cars.
    :expected_result: The cars sorted by price in ascending order.
    """
    expected_result = fake_cars_service.sorted_data_ascending_or_descending('price', False)
    assert expected_result == sorted(expected_result, key=lambda car: car.price)


def test_sorted_data_by_price_descending(fake_cars_service):
    """
    Test sorting car data by price in descending order.

    This test verifies that the sorted_data_ascending_or_descending method
    returns cars sorted by price in descending order. The expected result
    is checked against the actual output of the method.

    :param fake_cars_service: A CarService instance with predefined cars.
    :expected_result: The cars sorted by price in descending order.
    """
    expected_result = fake_cars_service.sorted_data_ascending_or_descending('price', True)
    assert expected_result == sorted(expected_result, key=lambda car: car.price, reverse=True)


def test_sorted_data_by_mileage_ascending(fake_cars_service):
    """
    Test sorting car data by mileage in ascending order.

    This test verifies that the sorted_data_ascending_or_descending method
    returns cars sorted by mileage in ascending order. The expected result
    is checked against the actual output of the method.

    :param fake_cars_service: A CarService instance with predefined cars.
    :expected_result: The cars sorted by mileage in ascending order.
    """
    expected_result = fake_cars_service.sorted_data_ascending_or_descending('mileage', False)
    assert expected_result == sorted(expected_result, key=lambda car: car.mileage)


def test_sorted_data_by_mileage_descending(fake_cars_service):
    """
    Test sorting car data by mileage in descending order.

    This test verifies that the sorted_data_ascending_or_descending method
    returns cars sorted by mileage in descending order. The expected result
    is checked against the actual output of the method.

    :param fake_cars_service: A CarService instance with predefined cars.
    :expected_result: The cars sorted by mileage in descending order.
    """
    expected_result = fake_cars_service.sorted_data_ascending_or_descending('mileage', True)
    assert expected_result == sorted(expected_result, key=lambda car: car.mileage, reverse=True)


def test_should_raise_error_for_invalid_attribute(fake_cars_service):
    """
    Test raising error for invalid attribute in sorting.

    This test checks that the sorted_data_ascending_or_descending method
    raises a ValueError when an invalid attribute is provided. The test
    ensures that the error message matches the expected output.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    with pytest.raises(ValueError):
        fake_cars_service.sorted_data_ascending_or_descending('invalid_attribute')


def test_should_return_empty_list_for_empty_list_sorted(fake_empty_cars_service):
    """
    Test sorting an empty list of cars.

    This test verifies that the sorted_data_ascending_or_descending method
    returns an empty list when there are no cars available in the repository.

    :param fake_empty_cars_service: A CarService instance with no cars.
    :expected_result: An empty list indicating no cars to sort.
    """
    assert fake_empty_cars_service.sorted_data_ascending_or_descending('price', False) == []

