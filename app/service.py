from app.model import Car
from dataclasses import dataclass
from app.repository import CarRepository
from collections import Counter, defaultdict

type CarItem = float | str | list[str]


@dataclass
class CarService:
    """
    A service class that provides various operations on car data, such as fetching attributes, sorting, filtering,
    and calculating statistics.

    :param car_repository: An instance of AbstractCarRepository used to retrieve car data.
    """

    car_repository: CarRepository

    def __call__(self):
        """
        Make the CarService class callable, returning the instance itself.

        :return: The CarService instance.
        """
        return self

    def get_attributes(self, attribute: str) -> CarItem:
        """
        Retrieve a list of values for a specified attribute from the car data.

        :param attribute: The car attribute to retrieve. Must be one of 'price', 'mileage', 'color', 'model', 'components', or 'id'.
        :return: A list of values corresponding to the specified attribute from all cars.
        :raises ValueError: If the attribute is invalid.
        """
        if attribute not in {'price', 'mileage', 'color', 'model', 'components', 'id'}:
            raise ValueError('Invalid attribute')
        cars = self.car_repository.get_data()
        return [getattr(car, attribute) for car in cars]

    def get_highest_value(self, attribute: str) -> float:
        """
        Get the highest value of a specified numeric attribute ('price' or 'mileage') from the car data.

        :param attribute: The attribute to find the highest value for ('price' or 'mileage').
        :return: The highest value of the specified attribute.
        :raises ValueError: If the attribute is not 'price' or 'mileage'.
        """
        if not attribute in {'price', 'mileage'}:
            raise ValueError('Attribute must be "price" or "mileage"')
        return max(self.get_attributes(attribute))

    def get_smallest_value(self, attribute: str) -> float:
        """
        Get the smallest value of a specified numeric attribute ('price' or 'mileage') from the car data.

        :param attribute: The attribute to find the smallest value for ('price' or 'mileage').
        :return: The smallest value of the specified attribute.
        :raises ValueError: If the attribute is not 'price' or 'mileage'.
        """
        if not attribute in {'price', 'mileage'}:
            raise ValueError('Attribute must be "price" or "mileage"')
        return min(self.get_attributes(attribute))

    def average_calculate(self, attribute: str) -> float:
        """
        Calculate the average value of a specified numeric attribute ('price' or 'mileage') from the car data.

        :param attribute: The attribute to calculate the average for ('price' or 'mileage').
        :return: The average value of the specified attribute.
        :raises ValueError: If the attribute is not 'price' or 'mileage'.
        """
        if not attribute in {'price', 'mileage'}:
            raise ValueError('Attribute must be "price" or "mileage"')
        return sum(self.get_attributes(attribute)) / len(self.car_repository.get_data())

    def sorted_data_ascending_or_descending(self, attribute: str, reverse=True) -> list[Car]:
        """
        Sort car data by a specified attribute in ascending or descending order.

        :param attribute: The attribute to sort by.
        :param reverse: Whether to sort in descending order (default is True).
        :return: A sorted list of Car objects by the specified attribute.
        """
        return sorted(self.car_repository.get_data(), key=lambda car: car.get_attribute(attribute), reverse=reverse)

    def filter_data_by_mileage(self, min_mileage: int) -> list[Car]:
        """
        Filter cars whose mileage is greater than the specified minimum value.

        :param min_mileage: The minimum mileage value.
        :return: A list of Car objects with mileage greater than min_mileage.
        """
        return list(filter(lambda car: car.has_mileage_greater_than(min_mileage), self.car_repository.get_data()))

    def count_cars_by_color(self) -> dict[str, int]:
        """
        Count the number of cars by color.

        :return: A dictionary with colors as keys and their respective counts as values.
        """
        count_colors = Counter([car.get_attribute('color') for car in self.car_repository.get_data()])
        return dict(count_colors.most_common())

    def the_most_expensive_models(self) -> dict[str, str]:
        """
        Get the model(s) of the most expensive car(s).

        :return: A dictionary with the model name as the key and the price as the value for the most expensive car(s).
        """
        return {car.get_attribute('model'): car.get_attribute('price') for car in self.car_repository.get_data() if
                car.get_attribute('price') == self.get_highest_value('price')}

    def cars_statistics(self, attribute: str) -> str:
        """
        Generate a summary of the highest, lowest, and average values for a specified numeric attribute.

        :param attribute: The attribute to generate statistics for ('price' or 'mileage').
        :return: A string summarizing the highest, lowest, and average values of the attribute.
        """
        return (f'The highest {attribute}: {self.get_highest_value(attribute)},'
                f' the lowest {attribute}: {self.get_smallest_value(attribute)},'
                f' the average {attribute}: {self.average_calculate(attribute)}.')

    def sort_car_components(self) -> list[Car]:
        """
        Sort the components list for each car in the repository.

        :return: A list of cars with sorted components.
        """
        return [car for car in self.car_repository.get_data() if getattr(car, 'components').sort() is None]

    def component_in_car(self) -> dict[str, list[str]]:
        """
        Create a mapping of components to the car models that contain those components.

        :return: A dictionary where the keys are component names and the values are lists of car models that include those components.
        """
        components_map = defaultdict(list)
        for car in self.car_repository.get_data():
            for component in getattr(car, 'components'):
                components_map[component].append(car.get_attribute('model'))
        return dict(sorted(components_map.items(), key=lambda item: len(item[1]), reverse=True))

    def cars_in_range(self, attribute: str, min_range: float, max_range: float) -> list[Car]:
        """
        Retrieve a list of cars with a specified attribute ('price' or 'mileage') within a given range.

        :param attribute: The attribute to filter by ('price' or 'mileage').
        :param min_range: The minimum value of the range.
        :param max_range: The maximum value of the range.
        :return: A list of Car objects whose specified attribute falls within the given range.
        :raises ValueError: If the attribute is not 'price' or 'mileage'.
        """
        if not attribute in {'price', 'mileage'}:
            raise ValueError('Attribute must be "price" or "mileage"')
        return [car for car in self.car_repository.get_data() if min_range < getattr(car, attribute) < max_range]

