from app.loader import JsonDataLoader, CsvDataLoader
from app.converter import ConvertDataToListCars
from app.validator import CarNumberElementValidator
from app.repository import CarRepository


def main() -> None:
    json_data = JsonDataLoader()
    print(json_data.load('data/data.json'))
    csv_data = CsvDataLoader()
    print(csv_data.load('data/data.csv'))
    # converter = ConvertDataToListCars()
    # validator = CarNumberElementValidator()
    # repository = CarRepository(json_data, converter, validator)
    # cars_from_json = repository.load_data('data/data.json')


if __name__ == '__main__':
    main()