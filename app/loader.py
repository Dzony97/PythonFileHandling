from abc import ABC, abstractmethod
import json
import csv
from typing import override
from app.converter import Data


class DataLoader(ABC):
    """
    Abstract base class for loading data from various file formats into a list of dictionaries.

    :param path: Path to the file containing data.
    :return: A list of dictionaries, each representing a car's attributes.
    """

    @abstractmethod
    def load(self, path: str) -> Data:
        """
        Load data from a file.

        :param path: The file path from which the data is to be loaded.
        :return: A list of dictionaries containing car attributes.
        """
        pass


class CsvDataLoader(DataLoader):
    """
    Loads car data from a CSV file and processes it into a list of dictionaries.

    :param path: The file path to the CSV file.
    :return: A list of dictionaries representing the car data. The 'price', 'mileage', and 'components' fields
             are parsed into appropriate types.
    """

    separator: str = ','

    @override
    def load(self, path: str) -> Data:
        """
        Load and parse car data from a CSV file.

        :param path: The file path to the CSV file.
        :return: A list of dictionaries where 'price' and 'mileage' are converted to integers, and 'components'
                 is split into a list of individual components.
        """
        with open(path) as csv_file:
            reader = [{key: val for key, val in row.items()} for row in csv.DictReader(csv_file)]
            for row in reader:
                row['price'], row['mileage'], row['components'] = (
                    int(row['price']),
                    int(row['mileage']),
                    [component.strip() for component in row['components'].split(self.separator)]
                )
            return reader


class JsonDataLoader(DataLoader):
    """
    Loads car data from a JSON file and returns it as a list of dictionaries.

    :param path: The file path to the JSON file.
    :return: A list of dictionaries representing the car data, retrieved under the 'cars' key.
    """

    key: str = 'cars'

    @override
    def load(self, path: str) -> Data:
        """
        Load and parse car data from a JSON file.

        :param path: The file path to the JSON file.
        :return: A list of dictionaries containing car attributes.
        """
        with open(path, 'r') as json_file:
            return json.load(json_file)[self.key]


class TxtDataLoader(DataLoader):
    """
    Loads car data from a plain text file, where each line represents a car and fields are separated by a delimiter.

    :param path: The file path to the text file.
    :return: A list of dictionaries representing the car data, with fields such as 'model', 'price', 'color',
             'mileage', and 'components' extracted from the line.
    """

    separator: str = ', '

    @override
    def load(self, path: str) -> Data:
        """
        Load and parse car data from a text file.

        :param path: The file path to the text file.
        :return: A list of dictionaries representing car data. Each line in the text file corresponds to one car,
                 with 'price' and 'mileage' converted to integers.
        """
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

