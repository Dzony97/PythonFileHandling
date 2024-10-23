import pytest
from .fake_objects import bmw_car


@pytest.mark.parametrize('test_input,expected', [("model", "BMW"), ("price", 260)])
def test_get_attribute(test_input, expected):
    """
    Test the get_attribute method of the Car class.

    This test checks if the get_attribute method correctly returns
    the value of the specified attribute from the bmw_car object.

    :param test_input: The name of the attribute to retrieve (string).
    :param expected: The expected value of the attribute.
    """
    assert bmw_car.get_attribute(test_input) == expected


def test_get_attribute_when_attribute_is_not_correct():
    """
    Test the get_attribute method when an invalid attribute is provided.

    This test verifies that a ValueError is raised when trying to access
    an attribute that does not exist in the Car class. The error message
    should indicate that the attribute is invalid.
    """
    with pytest.raises(ValueError) as err:
        car = bmw_car
        car.get_attribute('test')
    assert 'Invalid attribute' == str(err.value)


@pytest.mark.parametrize('test_input,expected', [(1300, True), (1500, False), (1399, True), (1400, False)])
def test_has_mileage_greater_than(test_input, expected):
    """
    Test the has_mileage_greater_than method of the Car class.

    This test checks if the has_mileage_greater_than method correctly
    determines whether the mileage of the bmw_car exceeds the given
    test_input value.

    :param test_input: The mileage value to compare against (integer).
    :param expected: The expected boolean result (True if the car's mileage
                     is greater than test_input, otherwise False).
    """
    assert bmw_car.has_mileage_greater_than(test_input) == expected

