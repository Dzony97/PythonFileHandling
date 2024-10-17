from app.loader import CsvDataLoader


def test_csv_loader():
    csv_loader = CsvDataLoader()
    excepted_result = [
        {'model': 'BMW', 'price': 120, 'color': 'BLACK', 'mileage': 1500, 'components': ['ABS', 'ALLOY WHEELS']},
        {'model': 'MAZDA', 'price': 160, 'color': 'WHITE', 'mileage': 2500,
         'components': ['AIR CONDITIONING', 'BLUETOOTH']}]
    assert csv_loader.load('C:\PROGRAMOWANIE\PythonFileHandling\data\data.csv') == excepted_result
