from abc import ABC, abstractmethod
import json
import csv


class DataLoader[T](ABC):

    @abstractmethod
    def load(self, path: str) -> list[dict[str, T]]:
        pass


class CsvDataLoader[T](DataLoader):
    separator: str = ','

    def load(self, path: str) -> list[dict[str, T]]:
        with open(path) as csv_file:
            reader = [{key: val for key, val in row.items()} for row in csv.DictReader(csv_file)]
            for row in reader:
                row['price'], row['mileage'], row['components'] = (int(row['price']), int(row['mileage']),
                                                                   [component.strip() for component in
                                                                    row['components'].split(self.separator)])
            return reader


class JsonDataLoader[T](DataLoader):
    key: str = 'cars'

    def load(self, path: str) -> list[dict[str, T]]:
        with open(path, 'r') as json_file:
            return json.load(json_file)[self.key]


class TxtDataLoader[T](DataLoader):
    separator: str = ', '

    def load(self, path: str) -> list[dict[str, T]]:
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
