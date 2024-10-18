from app.model import Car
from abc import ABC, abstractmethod
from typing import override

type Data[T] = list[dict[str, T]]


class Converter(ABC):
    @abstractmethod
    def convert(self, data: Data) -> list[Car]:
        pass


class ConvertDataToListCars(Converter):
    @override
    def convert(self, data: Data) -> list[Car]:
        return [Car(**car) for car in data]
