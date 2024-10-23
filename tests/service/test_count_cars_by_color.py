from .fake_cars_repository import fake_cars_service, fake_empty_cars_service


def test_count_cars_by_color(fake_cars_service):
    """
    Test that count_cars_by_color returns the correct count of cars
    grouped by their color.

    The test checks that the service correctly counts the number of cars
    for each color when there are multiple cars in the repository.

    :param fake_cars_service: A CarService instance with predefined cars.
    """
    expected_result = {'BLACK': 2, 'WHITE': 1}
    color_count = fake_cars_service.count_cars_by_color()
    assert color_count == expected_result


def test_count_cars_by_color_with_empty_data(fake_empty_cars_service):
    """
    Test that count_cars_by_color returns an empty dictionary when there
    are no cars in the repository.

    This test verifies that the service handles the case of an empty dataset
    correctly by returning an empty dictionary.

    :param fake_empty_cars_service: A CarService instance with no cars.
    """
    expected_result = {}
    color_count = fake_empty_cars_service.count_cars_by_color()
    assert color_count == expected_result
