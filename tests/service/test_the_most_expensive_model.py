from .fake_cars_repository import fake_cars_service, fake_empty_cars_service
from app.model import Car


def test_the_most_expensive_model(fake_cars_service):
    excepted_model = {'BMW': 260}
    most_expensive_model = fake_cars_service.the_most_expensive_models()
    assert excepted_model == most_expensive_model


def test_the_most_expensive_models(fake_cars_service):
    excepted_model = {'BMW': 260, 'MERCEDES': 260}
    fake_cars_service.car_repository._cars.append(
        Car(model='MERCEDES', price=260, color='RED', mileage=1200, components=['ABS', 'GPS']))
    most_expensive_models = fake_cars_service.the_most_expensive_models()
    assert excepted_model == most_expensive_models


def test_the_most_expensive_model_on_empty_database(fake_empty_cars_service):
    excepted_model = {}
    most_expensive_models = fake_empty_cars_service.the_most_expensive_models()
    assert excepted_model == most_expensive_models
