from app.loader import TxtDataLoader


def test_txt_loader():
    txt_loader = TxtDataLoader()
    excepted_result = [{'model': 'BMW', 'price': 120, 'color': 'BLACK', 'mileage': 1500, 'components':
        ['ABS', 'ALLOY WHEELS']}, {'model': 'MAZDA', 'price': 160, 'color': 'WHITE', 'mileage': 2500,
                                   'components': ['AIR CONDITIONING', 'BLUETOOTH']}]
    assert txt_loader.load('C:\PROGRAMOWANIE\PythonFileHandling\data\data.txt') == excepted_result
