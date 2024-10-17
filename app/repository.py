from dataclasses import dataclass
from abc import ABC, abstractmethod
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
