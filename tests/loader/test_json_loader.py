from app.loader import JsonDataLoader


def test_json_loader():
    """
    Test the JsonDataLoader class to ensure that it correctly loads and parses data from a JSON file.

    This test checks whether the JsonDataLoader correctly reads a JSON file containing car data
    and converts it into a list of dictionaries with the expected structure.

    The expected structure includes the following fields:
    - 'model': The model of the car (string).
    - 'price': The price of the car (integer).
    - 'color': The color of the car (string).
    - 'mileage': The mileage of the car (integer).
    - 'components': A list of components (list of strings).

    The test compares the loaded data with the expected result and raises an assertion error
    if the output does not match.

    :raises AssertionError: If the result from JsonDataLoader does not match the expected result.
    """
    json_loader = JsonDataLoader()
    expected_result = [
        {'model': 'AUDI', 'price': 170, 'color': 'BLACK', 'mileage': 1500, 'components': ['ABS', 'ALLOY WHEELS']},
        {'model': 'BMW', 'price': 260, 'color': 'BLACK', 'mileage': 1400, 'components': ['ABS', 'BLUETOOTH', 'ALLOY WHEELS']},
        {'model': 'MAZDA', 'price': 160, 'color': 'WHITE', 'mileage': 2500, 'components': ['AIR CONDITIONING', 'BLUETOOTH']},
        {'model': 'GOLF', 'price': 260, 'color': 'WHITE', 'mileage': 3500, 'components': ['AIR CONDITIONING', 'BLUETOOTH']}
    ]

    result = json_loader.load(r'C:\PROGRAMOWANIE\PythonFileHandling\data\data.json')

    assert result == expected_result
