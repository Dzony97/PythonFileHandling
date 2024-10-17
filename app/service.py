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
