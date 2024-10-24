from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override

type Data[T] = list[dict[str, T]]


class Validator(ABC):
    @abstractmethod
    def validate(self, data: Data) -> Data:
        pass


@dataclass
class CarNumberElementValidator(Validator):
    min_range: float = 0
    max_range: float = float('inf')
    component: str = "price"

    @override
    def validate(self, data: Data) -> Data:
        return [car for car in data if isinstance(car[self.component], int)
                and self.min_range < car[self.component] < self.max_range]


@dataclass
class CarStringElementValidator(Validator):
    min_length: int = 0
    max_length: int = 30
    component: str = "model"

    @override
    def validate(self, data: Data) -> Data:
        return [car for car in data if isinstance(car[self.component], str)
                and self.min_length < len(car[self.component]) < self.max_length]


@dataclass
class CarComponentsElementValidator(Validator):

    @override
    def validate(self, data: Data) -> Data:
        return [car for car in data if isinstance(car["components"], list) and
                all(isinstance(component, str) for component in car["components"])]
