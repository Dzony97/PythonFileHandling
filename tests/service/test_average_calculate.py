import pytest
from .fake_cars_repository import fake_cars_service


def test_should_raise_error_when_attribute_is_not_correct(fake_cars_service):
    """
    Test that the average_calculate method raises a ValueError
    when an invalid attribute is passed.
    """
    with pytest.raises(ValueError) as err:
        fake_cars_service.average_calculate('test')
    assert str(err.value) == 'Attribute must be "price" or "mileage"'


def test_should_calculate_average_when_attribute_is_correct(fake_cars_service):
    """
    Test that the average_calculate method returns a float
    when a valid attribute (mileage) is passed.
    """
    result = fake_cars_service.average_calculate('mileage')
    assert isinstance(result, float)


@pytest.mark.parametrize('test_input,expected', [('mileage', 1800), ('price', 200)])
def test_average_calculate_by_number_values(fake_cars_service, test_input, expected):
    """
    Test that the average_calculate method returns the expected
    average values for both mileage and price attributes.
    """
    assert fake_cars_service.average_calculate(test_input) == expected

