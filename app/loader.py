from abc import ABC, abstractmethod
import json
import csv


class DataLoader[T](ABC):

    @abstractmethod
    def load(self, path: str) -> list[dict[str, T]]:
        pass


class CSVLoader[T](DataLoader):
    separator = ','

    def load(self, path: str) -> list[dict[str, T]]:
        with open(path) as csv_file:
            reader = [{key: val for key, val in row.items()} for row in csv.DictReader(csv_file)]
            for row in reader:
                row['price'], row['mileage'], row['components'] = (int(row['price']), int(row['mileage']),
                                                                   [component.strip() for component in
                                                                    row['components'].split(self.separator)])
            return reader
