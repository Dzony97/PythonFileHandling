import pytest
from .fake_cars_repository import fake_cars_service


def test_should_raise_error_when_attribute_is_not_correct(fake_cars_service):
    """
    Test that an error is raised when an invalid attribute is specified.

    This test verifies that the service raises a ValueError when
    an invalid attribute name (not in the list of valid attributes)
    is passed to the get_highest_value method.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    with pytest.raises(ValueError) as err:
        fake_cars_service.get_highest_value('test')
    assert 'Attribute must be "price" or "mileage"' == str(err.value)


def test_should_return_value_when_attribute_is_correct(fake_cars_service):
    """
    Test that a value is returned when a valid attribute is specified.

    This test checks that the service correctly returns the highest
    value for a valid attribute (in this case, 'price'). It ensures
    that the returned value is of the expected type (integer).

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    result = fake_cars_service.get_highest_value('price')
    assert isinstance(result, int)


@pytest.mark.parametrize('test_input,expected', [('price', 260), ('mileage', 2500)])
def test_get_highest_value(fake_cars_service, test_input, expected):
    """
    Test retrieving the highest value for various attributes.

    This test verifies that the service correctly retrieves the
    highest value for specified valid attributes ('price' or 'mileage').
    It checks that the returned value matches the expected highest value.

    :param fake_cars_service: A CarService instance with predefined cars.
    :param test_input: The attribute name to retrieve the highest value for.
    :param expected: The expected highest value for the given attribute.
    """
    assert fake_cars_service.get_highest_value(test_input) == expected

