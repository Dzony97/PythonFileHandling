from app.loader import CsvDataLoader


def test_csv_loader():
    """
    Test the CsvDataLoader class to ensure that it correctly loads and parses data from a CSV file.

    This test checks whether the CsvDataLoader correctly reads a CSV file containing car data
    and converts it into a list of dictionaries with the expected structure.

    The expected structure includes the following fields:
    - 'model': The model of the car (string).
    - 'price': The price of the car (integer).
    - 'color': The color of the car (string).
    - 'mileage': The mileage of the car (integer).
    - 'components': A list of components (list of strings).

    The test compares the loaded data with the expected result and raises an assertion error
    if the output does not match.

    :raises AssertionError: If the result from CsvDataLoader does not match the expected result.
    """
    csv_loader = CsvDataLoader()
    expected_result = [
        {'model': 'BMW', 'price': 120, 'color': 'BLACK', 'mileage': 1500, 'components': ['ABS', 'ALLOY WHEELS']},
        {'model': 'MAZDA', 'price': 160, 'color': 'WHITE', 'mileage': 2500, 'components': ['AIR CONDITIONING', 'BLUETOOTH']}
    ]

    result = csv_loader.load(r'C:\PROGRAMOWANIE\PythonFileHandling\data\data.csv')

    assert result == expected_result

