from app.model import Car
from app.service import CarService
from app.repository import AbstractCarRepository
from dataclasses import dataclass, field
from typing import override
import pytest
from ..fake_objects import audi_car, bmw_car, mazda_car


@dataclass
class FakeCarRepository(AbstractCarRepository):
    _cars: list[Car] = field(default_factory=list)

    @override
    def load_data(self, filename: str):
        pass

    @override
    def get_data(self) -> list[Car]:
        return self._cars


@pytest.fixture
def fake_cars_service():
    cars = [audi_car, bmw_car, mazda_car]
    fake_repository = FakeCarRepository(cars)
    return CarService(fake_repository)


@pytest.fixture
def fake_empty_cars_service():
    return CarService(FakeCarRepository([]))
