from dataclasses import dataclass


@dataclass
class Car:
    model: str
    price: float
    color: str
    mileage: int
    components: list[str]

    def __str__(self):
        return (f'Model: {self.model}\n'
                f'Color: {self.color}\n'
                f'Price: ${self.price:,.2f}\n'
                f'Mileage: {self.mileage} km\n'
                f'Components: {', '.join(self.components) if self.components else ''}')

    def has_mileage_greater_than(self, min_value: int) -> bool:
        if 0 >= self.mileage or 0 >= min_value:
            raise ValueError('Mileage and min_value must be greater than zero')
        return self.mileage > min_value

    def get_attribute(self, attribute: str) -> str:
        if attribute not in {'price', 'mileage', 'color', 'model', 'components'}:
            raise ValueError('Invalid attribute')
        return getattr(self, attribute)
