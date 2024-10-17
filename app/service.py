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