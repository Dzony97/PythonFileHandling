from dataclasses import dataclass


@dataclass
class Car:
    """
    A class representing a car with attributes such as model, price, color, mileage, and components.

    :param model: The car's model name.
    :param price: The car's price in dollars.
    :param color: The color of the car.
    :param mileage: The mileage of the car in kilometers.
    :param components: A list of components the car has (e.g., features, parts).
    """

    model: str
    price: float
    color: str
    mileage: float
    components: list[str]

    def __str__(self):
        """
        Returns a string representation of the car's details.

        :return: A string describing the car's model, color, price, mileage, and components.
        """
        return (f'Model: {self.model}\n'
                f'Color: {self.color}\n'
                f'Price: ${self.price:,.2f}\n'
                f'Mileage: {self.mileage} km\n'
                f'Components: {", ".join(self.components) if self.components else ""}')

    def has_mileage_greater_than(self, min_value: int) -> bool:
        """
        Checks if the car's mileage is greater than a given minimum value.

        :param min_value: The minimum mileage to compare against.
        :return: True if the car's mileage is greater than min_value, False otherwise.
        :raises ValueError: If mileage or min_value is less than or equal to zero.
        """
        if 0 >= self.mileage or 0 >= min_value:
            raise ValueError('Mileage and min_value must be greater than zero')
        return self.mileage > min_value

    def get_attribute(self, attribute: str) -> str:
        """
        Returns the value of the specified attribute of the car.

        :param attribute: The attribute to retrieve. Must be one of 'price', 'mileage', 'color', 'model', or 'components'.
        :return: The value of the requested attribute as a string.
        :raises ValueError: If the specified attribute is invalid.
        """
        if attribute not in {'price', 'mileage', 'color', 'model', 'components'}:
            raise ValueError('Invalid attribute')
        return getattr(self, attribute)

