from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import override

from app.model import Car
from app.loader import DataLoader
from app.converter import Converter
from app.validator import Validator


@dataclass
class AbstractCarRepository(ABC):

    @abstractmethod
    def load_data(self, filename: str):
        pass

    @abstractmethod
    def get_data(self) -> list[Car]:
        pass


@dataclass
class CarRepository(AbstractCarRepository):
    loader: DataLoader
    converter: Converter
    validator: Validator

    _cars: list[Car] = field(default_factory=list, init=False)

    @override
    def load_data(self, filename: str) -> list[Car]:
        data = self.loader.load(filename)
        self.validator.validate(data)
        self._cars = self.converter.convert(data)
        return self._cars

    @override
    def get_data(self) -> list[Car]:
        return self._cars
