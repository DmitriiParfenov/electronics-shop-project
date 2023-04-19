import csv
import os.path

import pytest

PATH = os.path.join('tests', 'test_file.csv')


@pytest.fixture
def get_file_oversize_row():
    with open(PATH, 'w') as csvfile:
        fill = csv.writer(csvfile)
        fill.writerow(['name', 'price', 'quantity'])
        fill.writerow(['Очиститель', 20, 10, 5])
    return PATH


@pytest.fixture
def get_file_row_with_not_int():
    with open(PATH, 'w') as csvfile:
        fill = csv.writer(csvfile)
        fill.writerow(['name', 'price', 'quantity'])
        fill.writerow(['Очиститель', 20, 'a'])
    return PATH
