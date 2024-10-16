from dataclasses import dataclass


@dataclass
class Car:
    model: str
    price: float
    color: str
    mileage: int
    components: list[str]

    def __str__(self):
        components_str = ', '.join(self.components)
        return (f'Model: {self.model}\n'
                f'Color: {self.color}\n'
                f'Price: ${self.price:,.2f}\n'
                f'Mileage: {self.mileage} km\n'
                f'Components: {components_str if components_str else "None"}')