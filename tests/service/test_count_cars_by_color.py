from .fake_cars_repository import fake_cars_service, fake_empty_cars_service


def test_count_cars_by_color(fake_cars_service):
    expected_result = {'BLACK': 2, 'WHITE': 1}
    color_count = fake_cars_service.count_cars_by_color()
    assert color_count == expected_result


def test_count_cars_by_color_with_empty_data(fake_empty_cars_service):
    expected_result = {}
    color_count = fake_empty_cars_service.count_cars_by_color()
    assert color_count == expected_result
