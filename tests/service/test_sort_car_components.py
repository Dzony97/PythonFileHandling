from .fake_cars_repository import fake_cars_service, fake_empty_cars_service
from ..fake_objects import mazda_car, bmw_car, audi_car


def test_sort_car_components(fake_cars_service):
    """
    Test sorting car components with a standard dataset.

    This test verifies that the cars are sorted correctly based on their components.
    It checks that the expected order of cars matches the actual result from
    the sort_car_components method.

    :param fake_cars_service: A CarService instance with predefined cars.
    :expected_result: The expected sorted order of cars.
    """
    expected_result = [audi_car, bmw_car, mazda_car]
    assert expected_result == fake_cars_service.sort_car_components()


def test_sort_car_components_without_components(fake_cars_service):
    """
    Test sorting car components when one car has additional components.

    This test checks the behavior of the sort_car_components method when one
    of the cars (Mazda) is added to the repository after the initial sort
    is executed. The function ensures that the newly added car is included
    in the result, and the sort order remains consistent.

    :param fake_cars_service: A CarService instance with predefined cars.
    :expected_result: The expected sorted order of cars including the added Mazda.
    """
    expected_result = [audi_car, bmw_car, mazda_car, mazda_car]
    fake_cars_service.car_repository._cars.append(mazda_car)
    assert expected_result == fake_cars_service.sort_car_components()


def test_sort_car_components_by_empty_data(fake_empty_cars_service):
    """
    Test sorting car components with an empty dataset.

    This test verifies that the sort_car_components method returns an empty list
    when no cars are available in the repository. It ensures that the method
    handles empty datasets gracefully without errors.

    :param fake_empty_cars_service: A CarService instance with no cars.
    :expected_result: An empty list indicating no cars to sort.
    """
    expected_result = []
    assert expected_result == fake_empty_cars_service.sort_car_components()
