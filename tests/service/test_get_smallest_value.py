import pytest
from .fake_cars_repository import fake_cars_service


def test_should_raise_error_when_attribute_is_not_correct(fake_cars_service):
    with pytest.raises(ValueError) as err:
        fake_cars_service.get_smallest_value('test')
    assert 'Attribute must be "price" or "mileage"' == str(err.value)


def test_should_return_value_when_attribute_is_correct(fake_cars_service):
    result = fake_cars_service.get_smallest_value('price')
    assert isinstance(result, int)


@pytest.mark.parametrize('test_input,expected', [('price', 140), ('mileage', 1400)])
def test_get_smallest_value(fake_cars_service, test_input, expected):
    assert fake_cars_service.get_smallest_value(test_input) == expected
