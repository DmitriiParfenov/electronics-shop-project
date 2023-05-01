import pytest

from src.item import Item
from src.phone import Phone


def test_phone_issubclass(phone_example):
    assert issubclass(phone_example.__class__, Item) is True


@pytest.mark.parametrize("expected, name, price, quantity, number_of_sim", [(ValueError, "iPhone 14", 120_000, 5, "2"),
                                                                            (ValueError, "iPhone 14", 120_000, 5, 0),
                                                                            (ValueError, "iPhone 14", 120_000, 5, -5)])
def test_phone_validate_data(phone_example, expected, name, price, quantity, number_of_sim):
    with pytest.raises(expected):
        Phone(name, price, quantity, number_of_sim)


def test_phone_getter(phone_example):
    assert phone_example.number_of_sim == 2


@pytest.mark.parametrize("expected, number_of_sim", [(ValueError, 0),
                                                     (ValueError, -5)])
def test_phone_setter_1(phone_example, expected, number_of_sim):
    with pytest.raises(expected):
        phone_example.number_of_sim = number_of_sim


def test_phone_setter_2(phone_example):
    phone_example.number_of_sim = 5
    assert phone_example.number_of_sim == 5


def test_phone_repr(phone_example):
    assert repr(phone_example) == "Phone('iPhone 14', 120000, 5, 2)"


@pytest.mark.parametrize("index, expected", [(0, 'Класс Phone:'),
                                             (1, 'Name = iPhone 14'),
                                             (2, 'price = 120000'),
                                             (3, 'quantity = 5'),
                                             (4, 'total_price = 600000'),
                                             (5, 'SIM-card quantity = 2')])
def test_phone_str(phone_example, index, expected):
    result = []
    list_str_phone = str(phone_example).split('\n')
    for elem in list_str_phone:
        result.append(elem)
    assert result[index] == expected
