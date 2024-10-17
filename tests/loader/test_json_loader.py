from app.loader import JsonDataLoader


def test_json_loader():
    json_loader = JsonDataLoader()
    excepted_result =[{'model': 'AUDI', 'price': 170, 'color': 'BLACK', 'mileage': 1500, 'components': ['ABS', 'ALLOY WHEELS']},
                      {'model': 'BMW', 'price': 260, 'color': 'BLACK', 'mileage': 1400, 'components': ['ABS', 'BLUETOOTH', 'ALLOY WHEELS']},
                      {'model': 'MAZDA', 'price': 160, 'color': 'WHITE', 'mileage': 2500, 'components': ['AIR CONDITIONING', 'BLUETOOTH']},
                      {'model': 'GOLF', 'price': 260, 'color': 'WHITE', 'mileage': 3500, 'components': ['AIR CONDITIONING', 'BLUETOOTH']}]
    assert json_loader.load('C:\PROGRAMOWANIE\PythonFileHandling\data\data.json') == excepted_result