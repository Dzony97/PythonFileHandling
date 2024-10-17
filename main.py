from app.model import Car
from app.loader import JsonDataLoader, CsvDataLoader, TxtDataLoader
from app.converter import ConvertDataToListCars
from app.validator import CarNumberElementValidator


def main() -> None:
    json_data = JsonDataLoader()
    txt_data = TxtDataLoader()
    converter = ConvertDataToListCars()
    validator = CarNumberElementValidator()
    print(json_data.load('data/data.json'))


if __name__ == '__main__':
    main()