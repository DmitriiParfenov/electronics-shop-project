import csv
import os.path

import pytest

from src.item import Item
from src.phone import Phone

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


@pytest.fixture
def item_example():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone_example():
    return Phone("iPhone 14", 120_000, 5, 2)
