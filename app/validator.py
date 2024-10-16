from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar

T = TypeVar('T')
Data = list[dict[str, T]]


class Validator[T](ABC):
    @abstractmethod
    def validate(self, data: Data) -> Data:
        pass


@dataclass
class CarNumberElementValidator(Validator):
    min_range: float = 0
    max_range: float = float('inf')
    component: str = "price"

    def validate(self, data: Data) -> Data:
        return [car for car in data if isinstance(car[self.component], int)
                and self.min_range < car[self.component] < self.max_range]
