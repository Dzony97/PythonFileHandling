from .fake_cars_repository import fake_empty_cars_service, fake_cars_service


def test_components_in_car(fake_cars_service):
    excepted_result = {'BLUETOOTH': ['BMW', 'MAZDA'], 'ABS': ['AUDI', 'BMW'], 'ALLOY WHEELS': ['AUDI', 'BMW'], 'AIR CONDITIONING': ['MAZDA']}
    assert excepted_result == fake_cars_service.component_in_car()


def test_components_in_car_with_empty_data(fake_empty_cars_service):
    excepted_result = {}
    assert excepted_result == fake_empty_cars_service.component_in_car()
