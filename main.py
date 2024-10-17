from app.model import Car
from app.loader import JsonDataLoader, CsvDataLoader, TxtDataLoader
from app.converter import ConvertDataToListCars
from app.validator import CarNumberElementValidator


def main() -> None:
    json_data = JsonDataLoader()
    txt_data = TxtDataLoader()
    converter = ConvertDataToListCars()
    validator = CarNumberElementValidator()
    print(txt_data.load('data/data.txt'))


if __name__ == '__main__':
    main()