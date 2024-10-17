from app.model import Car
from app.repository import AbstractCarRepository
from dataclasses import dataclass, field
from typing import override
import pytest


@dataclass
class FakeCarRepository(AbstractCarRepository):
    _cars: list[Car] = field(default_factory=list)

    @override
    def load_data(self, filename: str):
        pass

    @override
    def get_data(self) -> list[Car]:
        return self._cars
