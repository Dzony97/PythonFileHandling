from abc import ABC, abstractmethod
import json
import csv
from typing import override

type Data[T] = list[dict[str, T]]


class DataLoader(ABC):

    @abstractmethod
    def load(self, path: str) -> Data:
        pass


class CsvDataLoader(DataLoader):
    separator: str = ','

    @override
    def load(self, path: str) -> Data:
        with open(path) as csv_file:
            reader = [{key: val for key, val in row.items()} for row in csv.DictReader(csv_file)]
            for row in reader:
                row['price'], row['mileage'], row['components'] = (int(row['price']), int(row['mileage']),
                                                                   [component.strip() for component in
                                                                    row['components'].split(self.separator)])
            return reader


class JsonDataLoader(DataLoader):
    key: str = 'cars'

    @override
    def load(self, path: str) -> Data:
        with open(path, 'r') as json_file:
            return json.load(json_file)[self.key]


class TxtDataLoader(DataLoader):
    separator: str = ', '

    @override
    def load(self, path: str) -> Data:
        cars = []
        with open(path, 'r') as txt_file:
            for line in txt_file:
                component = line.strip().split(self.separator)
                cars_elements = {
                    'model': component[0],
                    'price': int(component[1]),
                    'color': component[2],
                    'mileage': int(component[3]),
                    'components': component[4:]
                }
                cars.append(cars_elements)
            return cars
