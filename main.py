from app.model import Car
from app.loader import JsonDataLoader
from app.converter import ConvertDataToListCars


def main() -> None:
    json_data = JsonDataLoader()
    converter = ConvertDataToListCars()
    print(converter.convert(json_data.load('data/data.json')))


if __name__ == '__main__':
    main()