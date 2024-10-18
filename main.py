from app.loader import JsonDataLoader
from app.converter import ConvertDataToListCars
from app.validator import CarNumberElementValidator
from app.repository import CarRepository


def main() -> None:
    json_data = JsonDataLoader()
    converter = ConvertDataToListCars()
    validator = CarNumberElementValidator()
    repository = CarRepository(json_data, converter, validator)
    cars_from_json = repository.load_data('data/data.json')
    print(cars_from_json)


if __name__ == '__main__':
    main()