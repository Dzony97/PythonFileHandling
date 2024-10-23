from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import override

from app.model import Car
from app.loader import DataLoader
from app.converter import Converter
from app.validator import Validator


@dataclass
class AbstractCarRepository(ABC):
    """
    Abstract base class for car repositories, defining the interface for loading and retrieving car data.
    """

    @abstractmethod
    def load_data(self, filename: str):
        """
        Load car data from the specified file.

        :param filename: The name of the file to load data from.
        :return: A list of Car objects.
        """
        pass

    @abstractmethod
    def get_data(self) -> list[Car]:
        """
        Retrieve the loaded car data.

        :return: A list of Car objects.
        """
        pass


@dataclass
class CarRepository(AbstractCarRepository):
    """
    A repository for loading, validating, and converting car data into a list of Car objects.

    :param loader: An instance of DataLoader used to load data from a file.
    :param converter: An instance of Converter used to convert raw data into Car objects.
    :param validator: An instance of Validator used to validate the raw data.
    :param _cars: A private list storing the loaded and converted Car objects.
    """

    loader: DataLoader
    converter: Converter
    validator: Validator

    _cars: list[Car] = field(default_factory=list, init=False)

    @override
    def load_data(self, filename: str) -> list[Car]:
        """
        Load, validate, and convert car data from a file.

        :param filename: The name of the file to load data from.
        :return: A list of Car objects after validation and conversion.
        """
        data = self.loader.load(filename)
        self.validator.validate(data)
        self._cars = self.converter.convert(data)
        return self._cars

    @override
    def get_data(self) -> list[Car]:
        """
        Retrieve the list of Car objects that were loaded and converted.

        :return: A list of Car objects.
        """
        return self._cars
