from app.model import Car
from dataclasses import dataclass
from app.repository import AbstractCarRepository


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
