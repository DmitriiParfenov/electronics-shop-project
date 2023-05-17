import pytest

from src.item import InstantiateCSVError
from src.item import Item


@pytest.fixture
def get_list_from_class_object(item_example):
    list_from_class = str(item_example).split('\n')
    return list_from_class


@pytest.fixture
def get_list_from_class_object(item_example):
    list_from_class = str(item_example).split('\n')
    return list_from_class


@pytest.mark.parametrize('expected, name, price, quantity', [(ValueError, 10, 10000, 20),
                                                             (ValueError, "Смартфон", "10000", 20),
                                                             (ValueError, "Смартфон", 10000, "20")])
def test_item_validate_data(expected, name, price, quantity):
    """Валидация входных данных при инициализации экземпляров класса"""
    with pytest.raises(expected):
        Item(name, price, quantity)


def test_item_calculate_total_price(item_example):
    """При создании экземпляра класса рассчитывается общая стоимость товара и при вызове calculate_total_price()
    возвращается общая стоимость товара"""
    assert item_example.calculate_total_price() == 200000


def test_item_apply_discount(item_example):
    """Вызывая apply_discount() мы можем изменить цену товара в зависимости от величины pay_rate."""
    item_example.pay_rate = 0.8
    item_example.apply_discount()
    assert item_example.price == 8000


def test_item_name_property(item_example):
    """При обращении к приватному атрибуту извне должен возвращать его значение"""
    assert item_example.name == "Смартфон"


@pytest.mark.parametrize("expected, name", [(ValueError, 10),
                                            (ValueError, 'panasonictechnics'),
                                            (ValueError, {'panasonic': 'technics'})])
def test_item_name_setter_validate_date(item_example, name, expected):
    """Название товара должно быть строкой и длиной не более 10 символов"""
    with pytest.raises(expected):
        item_example.name = name


def test_item_name_setter(item_example):
    """Название товара должно быть строкой и длиной не более 10 символов"""
    item_example.name = 'пылесос'
    assert item_example.name == 'пылесос'


def test_item_instantiate_from_csv_validate_data_1(item_example, get_file_oversize_row):
    """При открытии файла с неверным количеством столбцов возбуждается исключение InstantiateCSVError"""
    with pytest.raises(InstantiateCSVError):
        item_example.instantiate_from_csv('test_file.csv')


def test_item_instantiate_from_csv_validate_data_2(item_example, get_file_row_with_not_int):
    """При открытии файла с неверно заданными данными метод возвращает оповестительную строку"""
    assert item_example.instantiate_from_csv('test_file.csv') == 'Проверьте содержимое файла:' \
                                                                 'name — это строка, price — это integer ' \
                                                                 'или float, а quantity — это integer.\n'


def test_item_instantiate_from_csv_validate_data_3(item_example, get_file_row_with_not_int):
    """Если нет заданного файла в текущей дериктории, то возбуждается исключение FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        item_example.instantiate_from_csv('not_exists.csv')


def test_item_instantiate_from_csv_validate_data_4(item_example, get_broken_file):
    """При открытии файла с неверным количеством столбцов возбуждается исключение InstantiateCSVError"""
    with pytest.raises(InstantiateCSVError):
        item_example.instantiate_from_csv('test_file.csv')


@pytest.mark.parametrize("argument, expected", [('5', 5), ('5.0', 5), ('5.5', 5),
                                                ('dfbdfbdf', 'user_str должен содержать int или float')])
def test_item_string_to_number(item_example, argument, expected):
    """Цена и количество товаров должна иметь тип float или int"""
    assert item_example.string_to_number(argument) == expected


def test_item_repr(item_example):
    """Метод __repr__ должен возвращать строку с названием класса и полями при инизиализации экземпляров класса"""
    assert repr(item_example) == "Item('Смартфон', 10000, 20)"


@pytest.mark.parametrize("index, expected", [(0, 'Класс Item:'),
                                             (1, 'Name = Смартфон'),
                                             (2, 'price = 10000'),
                                             (3, 'quantity = 20'),
                                             (4, 'total_price = 200000')])
def test_item_str(get_list_from_class_object, index, expected):
    """Метод __repr__ должен возвращать строку с названием класса и полями при инизиализации экземпляров класса
    в дружественном формате"""
    assert get_list_from_class_object[index] == expected


def test_item_add_1(item_example, phone_example):
    """Метод __add__ должен складывать количество товаров по полю 'quantity' у экземпляров классов,
    унаследованных от класса Item"""
    assert item_example + phone_example == 25


@pytest.mark.parametrize("expected, number", [(ValueError, 25),
                                              (ValueError, 0),
                                              (ValueError, -100)])
def test_item_add_2(item_example, expected, number):
    """Метод __add__ должен складывать количество товаров по полю 'quantity' у экземпляров классов,
    унаследованных от класса Item"""
    with pytest.raises(expected):
        item_example + number
