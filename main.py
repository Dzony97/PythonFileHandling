from app.model import Car
from app.loader import JsonDataLoader
from app.converter import ConvertDataToListCars
from app.validator import CarNumberElementValidator


def main() -> None:
    json_data = JsonDataLoader()
    converter = ConvertDataToListCars()
    validator = CarNumberElementValidator()
    print(converter.convert(validator.validate(json_data.load('data/data.json'))))


if __name__ == '__main__':
    main()