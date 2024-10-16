from abc import ABC, abstractmethod
import json
import csv


class DataLoader[T](ABC):

    @abstractmethod
    def load(self, path: str) -> list[dict[str, T]]:
        pass
