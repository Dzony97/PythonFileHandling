from app.model import Car
from app.loader import JsonDataLoader, CsvDataLoader
from app.converter import ConvertDataToListCars
from app.validator import CarNumberElementValidator


def main() -> None:
    json_data = JsonDataLoader()
    csv_data = CsvDataLoader()
    converter = ConvertDataToListCars()
    validator = CarNumberElementValidator()
    print(csv_data.load('data/data.csv'))


if __name__ == '__main__':
    main()