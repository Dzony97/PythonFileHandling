from app.model import Car
from abc import ABC, abstractmethod
from typing import override

from app.loader import CarData


class Converter(ABC):
    """
    Abstract base class that defines the interface for converting data into a list of Car objects.

    :param data: Data in the form of a list of dictionaries where each dictionary represents a car's attributes.
    :return: A list of Car objects.
    """

    @abstractmethod
    def convert(self, data: CarData) -> list[Car]:
        """
        Convert data into a list of Car objects.

        :param data: A list of dictionaries containing car attributes.
        :return: A list of Car objects.
        """
        pass


class ConvertDataToListCars(Converter):
    """
    Concrete implementation of Converter that converts a list of dictionaries into a list of Car objects.

    :param data: A list of dictionaries where each dictionary contains attributes for a car.
    :return: A list of Car objects created from the input data.
    """

    @override
    def convert(self, data: CarData) -> list[Car]:
        """
        Convert a list of dictionaries into a list of Car objects.

        :param data: A list of dictionaries representing car attributes.
        :return: A list of Car objects created by unpacking the dictionary values.
        """
        return [Car(**car) for car in data]

