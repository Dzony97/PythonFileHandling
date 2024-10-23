from .fake_cars_repository import fake_cars_service, fake_empty_cars_service
from app.model import Car


def test_the_most_expensive_model(fake_cars_service):
    """
    Test retrieval of the most expensive car model from a service.

    This test verifies that the method `the_most_expensive_models` correctly identifies
    the most expensive model from the provided car data. The expected result is checked
    against the actual output of the method.

    :param fake_cars_service: A CarService instance with predefined cars.
    :expected_model: A dictionary containing the most expensive model and its price.
    """
    expected_model = {'BMW': 260}
    most_expensive_model = fake_cars_service.the_most_expensive_models()
    assert expected_model == most_expensive_model


def test_the_most_expensive_models(fake_cars_service):
    """
    Test retrieval of multiple most expensive car models.

    This test verifies that the method `the_most_expensive_models` can identify
    multiple car models with the same highest price. The expected result is checked
    against the actual output of the method.

    :param fake_cars_service: A CarService instance with predefined cars.
    :expected_model: A dictionary containing the most expensive models and their prices.
    """
    expected_model = {'BMW': 260, 'MERCEDES': 260}
    fake_cars_service.car_repository._cars.append(
        Car(model='MERCEDES', price=260, color='RED', mileage=1200, components=['ABS', 'GPS']))
    most_expensive_models = fake_cars_service.the_most_expensive_models()
    assert expected_model == most_expensive_models


def test_the_most_expensive_model_on_empty_database(fake_empty_cars_service):
    """
    Test retrieval of most expensive car models from an empty database.

    This test verifies that the method `the_most_expensive_models` returns an empty
    dictionary when there are no cars in the repository. The expected result is checked
    against the actual output of the method.

    :param fake_empty_cars_service: A CarService instance with no cars.
    :expected_model: An empty dictionary indicating no cars are available.
    """
    expected_model = {}
    most_expensive_models = fake_empty_cars_service.the_most_expensive_models()
    assert expected_model == most_expensive_models
