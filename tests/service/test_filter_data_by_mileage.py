from .fake_cars_repository import fake_cars_service, fake_empty_cars_service
from ..fake_objects import mazda_car


def test_filter_data_by_mileage_various_mileage(fake_cars_service):
    """
    Test filtering cars by mileage when some cars have mileage greater
    than the specified value.

    This test verifies that the service correctly filters out cars that
    have mileage greater than 1000. It checks that the returned list matches
    the expected filtered results based on the mileage criteria.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    expected_result = fake_cars_service.filter_data_by_mileage(1000)
    assert expected_result == list(filter(lambda car: car.has_mileage_greater_than(1000), expected_result))


def test_filter_data_by_empty_list(fake_empty_cars_service):
    """
    Test filtering cars by mileage when the car repository is empty.

    This test verifies that the service returns an empty list when
    there are no cars in the repository, regardless of the mileage
    criteria provided.

    :param fake_empty_cars_service: A CarService instance with no cars.
    """
    expected_result = []
    assert expected_result == fake_empty_cars_service.filter_data_by_mileage(10)


def test_filter_data_by_mileage_exact_boundary(fake_cars_service):
    """
    Test filtering cars by mileage when the specified mileage matches
    the exact boundary of a car's mileage.

    This test checks that the service correctly identifies and includes
    cars that have mileage equal to the specified boundary value.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    expected_result = [mazda_car]
    assert expected_result == fake_cars_service.filter_data_by_mileage(1500)


def test_filter_data_by_mileage_all_below(fake_cars_service):
    """
    Test filtering cars by mileage when all cars have mileage below
    the specified threshold.

    This test verifies that the service returns an empty list when
    the mileage filter is set higher than the mileage of all cars
    in the repository.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    result = fake_cars_service.filter_data_by_mileage(2600)
    assert [] == result
