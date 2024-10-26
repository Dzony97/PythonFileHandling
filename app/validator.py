from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override
from app.service import CarItem

type Data = list[dict[str, CarItem]]


class Validator(ABC):
    """
    Abstract base class for validating car data. Defines the interface for validation.
    """

    @abstractmethod
    def validate(self, data: Data) -> Data:
        """
        Validate car data based on specific criteria.

        :param data: A list of dictionaries representing car data.
        :return: A list of dictionaries representing valid car data after validation.
        """
        pass


@dataclass
class CarNumberElementValidator(Validator):
    """
    A validator for numeric elements (e.g., 'price') in car data.

    :param min_range: The minimum acceptable value for the numeric element (default is 0).
    :param max_range: The maximum acceptable value for the numeric element (default is infinity).
    :param component: The car component to validate (default is 'price').
    """

    min_range: float = 0
    max_range: float = float('inf')
    component: str = "price"

    @override
    def validate(self, data: Data) -> Data:
        """
        Validate that the numeric component is within the specified range.

        :param data: A list of dictionaries representing car data.
        :return: A list of dictionaries where the specified numeric component falls within the min_range and max_range.
        """
        return [car for car in data if isinstance(car[self.component], int)
                and self.min_range < car[self.component] < self.max_range]


@dataclass
class CarStringElementValidator(Validator):
    """
    A validator for string elements (e.g., 'model') in car data.

    :param min_length: The minimum acceptable length for the string component (default is 0).
    :param max_length: The maximum acceptable length for the string component (default is 30).
    :param component: The car component to validate (default is 'model').
    """

    min_length: int = 0
    max_length: int = 30
    component: str = "model"

    @override
    def validate(self, data: Data) -> Data:
        """
        Validate that the string component's length is within the specified range.

        :param data: A list of dictionaries representing car data.
        :return: A list of dictionaries where the specified string component's length is within the min_length and max_length.
        """
        return [car for car in data if isinstance(car[self.component], str)
                and self.min_length < len(car[self.component]) < self.max_length]


@dataclass
class CarComponentsElementValidator(Validator):
    """
    A validator for the 'components' list element in car data.

    This ensures that the 'components' field is a list and that all elements in the list are strings.
    """

    @override
    def validate(self, data: Data) -> Data:
        """
        Validate that the 'components' field is a list of strings.

        :param data: A list of dictionaries representing car data.
        :return: A list of dictionaries where the 'components' field is a list of strings.
        """
        return [car for car in data if isinstance(car["components"], list) and
                all(isinstance(component, str) for component in car["components"])]

