import pytest
from .fake_objects import bmw_car


@pytest.mark.parametrize('test_input,expected', [("model", "BMW"), ("price", 260)])
def test_get_attribute(test_input, expected):
    assert bmw_car.get_attribute(test_input) == expected


def test_get_attribute_when_attribute_is_not_correct():
    with pytest.raises(ValueError) as err:
        car = bmw_car
        car.get_attribute('test')
    assert 'Invalid attribute' == str(err.value)


@pytest.mark.parametrize('test_input,expected', [(1300, True), (1500, False), (1399, True), (1400, False)])
def test_has_mileage_greater_than(test_input, expected):
    assert bmw_car.has_mileage_greater_than(test_input) == expected
