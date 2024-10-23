from .fake_cars_repository import fake_empty_cars_service, fake_cars_service


def test_components_in_car(fake_cars_service):
    """
    Test that component_in_car returns the correct mapping of components to car models.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    expected_result = {
        'BLUETOOTH': ['BMW', 'MAZDA'],
        'ABS': ['AUDI', 'BMW'],
        'ALLOY WHEELS': ['AUDI', 'BMW'],
        'AIR CONDITIONING': ['MAZDA']
    }
    assert expected_result == fake_cars_service.component_in_car()


def test_components_in_car_with_empty_data(fake_empty_cars_service):
    """
    Test that component_in_car returns an empty dictionary when no cars are present.

    :param fake_empty_cars_service: A CarService instance with no cars.
    """
    expected_result = {}
    assert expected_result == fake_empty_cars_service.component_in_car()
