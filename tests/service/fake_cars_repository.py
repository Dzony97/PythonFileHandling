from app.model import Car
from app.service import CarService
from app.repository import AbstractRepository, CarRepository
from dataclasses import dataclass, field
from typing import override
import pytest
from ..fake_objects import audi_car, bmw_car, mazda_car


@dataclass
class FakeCarRepository(CarRepository):

    def __init__(self, cars: list[Car]):
        self._cars = cars if cars else []

    """
    A fake implementation of the AbstractCarRepository for testing purposes.

    This class provides a way to mock car data without relying on actual file I/O.
    It allows the tests to use predefined car objects.
    """


    @override
    def load_data(self, filename: str) -> list[Car]:
        """
        This method is intentionally left unimplemented as it is not needed for the tests.
        """
        return self._cars

    @override
    def get_data(self) -> list[Car]:
        """
        Return the list of Car objects stored in this fake repository.

        :return: A list of Car objects.
        """
        return self._cars


@pytest.fixture
def fake_cars_service():
    """
    Fixture to create a CarService instance with predefined car data.

    This fixture initializes a FakeCarRepository with sample car objects and
    returns a CarService instance for testing.

    :return: An instance of CarService populated with fake car data.
    """
    cars = [audi_car, bmw_car, mazda_car]
    fake_repository = FakeCarRepository(cars)
    return CarService(fake_repository)


@pytest.fixture
def fake_empty_cars_service():
    """
    Fixture to create a CarService instance with an empty car repository.

    This fixture returns a CarService instance with a FakeCarRepository that
    contains no car data, useful for testing edge cases.

    :return: An instance of CarService with no cars.
    """
    return CarService(FakeCarRepository([]))

