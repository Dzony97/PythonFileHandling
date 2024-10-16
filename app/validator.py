from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar

T = TypeVar('T')
Data = list[dict[str, T]]


class Validator[T](ABC):
    @abstractmethod
    def validate(self, data: Data) -> Data:
        pass