from app.model import Car
from dataclasses import dataclass
from app.repository import AbstractCarRepository
from collections import Counter, defaultdict

@dataclass
class CarService[T]:
    car_repository: AbstractCarRepository

    def get_attributes(self, attribute: str) -> list[T]:
        if attribute not in {'price', 'mileage', 'color', 'model', 'components', 'id'}:
            raise ValueError('Invalid attribute')
        cars = self.car_repository.get_data()
        return [getattr(car, attribute) for car in cars]

    def get_highest_value(self, attribute: str) -> float:
        if not attribute in {'price', 'mileage'}:
            raise ValueError('Attribute must be "price" or "mileage"')
        return max(self.get_attributes(attribute))

    def get_smallest_value(self, attribute: str) -> float:
        if not attribute in {'price', 'mileage'}:
            raise ValueError('Attribute must be "price" or "mileage"')
        return min(self.get_attributes(attribute))

    def average_calculate(self, attribute: str) -> float:
        if not attribute in {'price', 'mileage'}:
            raise ValueError('Attribute must be "price" or "mileage"')
        return sum(self.get_attributes(attribute)) / len(self.car_repository.get_data())

    def sorted_data_ascending_or_descending(self, attribute: str, reverse=True) -> list[Car]:
        return sorted(self.car_repository.get_data(), key=lambda car: car.get_attribute(attribute), reverse=reverse)

    def filter_data_by_mileage(self, min_mileage: int) -> list[Car]:
        return list(filter(lambda car: car.has_mileage_greater_than(min_mileage), self.car_repository.get_data()))

    def count_cars_by_color(self) -> dict[str, int]:
        count_colors = Counter([car.get_attribute('color') for car in self.car_repository.get_data()])
        return dict(count_colors.most_common())

    def the_most_expensive_models(self) -> dict[str, str]:
        return {car.get_attribute('model'): car.get_attribute('price') for car in self.car_repository.get_data() if
                car.get_attribute('price') == self.get_highest_value('price')}

    def cars_statistics(self, attribute: str) -> str:
        return (f'The highest {attribute}: {self.get_highest_value(attribute)},'
                f' the lowest {attribute}: {self.get_smallest_value(attribute)},'
                f' the average {attribute}: {self.average_calculate(attribute)}.')

    def sort_car_components(self) -> list[Car]:
        return [car for car in self.car_repository.get_data() if getattr(car, 'components').sort() is None]

    def component_in_car(self) -> dict[str, list[str]]:
        components_map = defaultdict(list)
        for car in self.car_repository.get_data():
            for component in getattr(car, 'components'):
                components_map[component].append(car.get_attribute('model'))
        return dict(sorted(components_map.items(), key=lambda item: len(item[1]), reverse=True))

    def cars_in_range(self, attribute: str, min_range: float, max_range: float) -> list[Car]:
        if not attribute in {'price', 'mileage'}:
            raise ValueError('Attribute must be "price" or "mileage"')
        return [car for car in self.car_repository.get_data() if min_range < getattr(car, attribute) < max_range]
