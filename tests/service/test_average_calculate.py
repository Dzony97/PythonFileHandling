import pytest
from .fake_cars_repository import fake_cars_service


def test_should_raise_error_when_attribute_is_not_correct(fake_cars_service):
    with pytest.raises(ValueError) as err:
        fake_cars_service.average_calculate('test')
    assert 'Attribute must be "price" or "mileage"' == str(err.value)


def test_should_calculate_average_when_attribute_is_correct(fake_cars_service):
    result = fake_cars_service.average_calculate('mileage')
    assert isinstance(result, float)


@pytest.mark.parametrize('test_input,expected', [('mileage', 1800), ('price', 200)])
def test_average_calculate_by_number_values(fake_cars_service, test_input, expected):
    assert fake_cars_service.average_calculate(test_input) == expected
