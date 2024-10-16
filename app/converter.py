from app.model import Car
from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar('T')
Data = list[dict[str, T]]


class Converter(ABC):
    @abstractmethod
    def convert(self, data: Data) -> list[Car]:
        pass
