import pytest
from .fake_cars_repository import fake_cars_service


def test_when_attribute_is_not_correct(fake_cars_service):
    """
    Test retrieving car attributes when an invalid attribute is specified.

    This test verifies that the service raises a ValueError when
    an invalid attribute name (not in the list of valid attributes)
    is passed to the get_attributes method.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    with pytest.raises(ValueError) as err:
        cars = fake_cars_service()
        cars.get_attributes('test')
    assert 'Invalid attribute' == str(err.value)


def test_when_attribute_is_correct(fake_cars_service):
    """
    Test retrieving car attributes when a valid attribute is specified.

    This test checks that the service correctly retrieves the values
    of a specified valid attribute (in this case, 'model') from
    all cars in the repository. It ensures that the retrieved
    list matches the expected list of models.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    cars = fake_cars_service()
    assert cars.get_attributes('model') == ['AUDI', 'BMW', 'MAZDA']
