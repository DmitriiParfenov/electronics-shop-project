import csv
import os.path
import pytest

from src.item import Item
from src.keyboard import Keyboard
from src.phone import Phone

PATH = os.path.join('test_file.csv')


@pytest.fixture
def get_file_oversize_row():
    with open(PATH, 'w') as csvfile:
        fill = csv.writer(csvfile)
        fill.writerow(['name', 'price', 'quantity'])
        fill.writerow(['Очиститель', 20, 10, 5])


@pytest.fixture
def get_file_row_with_not_int():
    with open(PATH, 'w') as csvfile:
        fill = csv.writer(csvfile)
        fill.writerow(['name', 'price', 'quantity'])
        fill.writerow(['Очиститель', 20, 'a'])


@pytest.fixture
def get_broken_file():
    with open(PATH, 'w') as csvfile:
        fill = csv.writer(csvfile)
        fill.writerow(['name', 'price'])
        fill.writerow(['Очиститель', 20, 30])


@pytest.fixture
def item_example():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone_example():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def keyboard_example():
    return Keyboard('Dark Project KD87A', 9600, 5)
