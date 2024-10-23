import pytest
from .fake_cars_repository import fake_cars_service


def test_should_raise_error_when_attribute_is_not_correct(fake_cars_service):
    """
    Test that an error is raised when an invalid attribute is specified.

    This test verifies that the service raises a ValueError when
    an invalid attribute name (not in the list of valid attributes)
    is passed to the get_smallest_value method.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    with pytest.raises(ValueError) as err:
        fake_cars_service.get_smallest_value('test')
    assert 'Attribute must be "price" or "mileage"' == str(err.value)


def test_should_return_value_when_attribute_is_correct(fake_cars_service):
    """
    Test that a value is returned when a valid attribute is specified.

    This test checks that the service correctly returns the smallest
    value for a valid attribute (in this case, 'price'). It ensures
    that the returned value is of the expected type (integer).

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    result = fake_cars_service.get_smallest_value('price')
    assert isinstance(result, int)


@pytest.mark.parametrize('test_input,expected', [('price', 140), ('mileage', 1400)])
def test_get_smallest_value(fake_cars_service, test_input, expected):
    """
    Test retrieving the smallest value for various attributes.

    This test verifies that the service correctly retrieves the
    smallest value for specified valid attributes ('price' or 'mileage').
    It checks that the returned value matches the expected smallest value.

    :param fake_cars_service: A CarService instance with predefined cars.
    :param test_input: The attribute name to retrieve the smallest value for.
    :param expected: The expected smallest value for the given attribute.
    """
    assert fake_cars_service.get_smallest_value(test_input) == expected
