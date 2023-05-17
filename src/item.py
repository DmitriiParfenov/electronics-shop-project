import csv
import os.path
from typing import Union


class InstantiateCSVError(Exception):
    """Класс исключений при повреждении файла формата csv, из которого добавляются элементы при инициализации
    экземпляра класса Item"""
    def __init__(self, way: str):
        """
        Создание экземпляра класса InstantiateCSVError.
        :param way: Название файла.
        При возбуждении исключения будет выводиться сообщение, которое определено в self.message.
        """
        self.way = way
        self.message = f'Файл {self.way} поврежден'

    def __str__(self):
        """Возвращает строку с оповещением при возбуждении текущего исключения."""
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: Union[int, float], quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        if not isinstance(name, str):
            raise ValueError('name should be string')
        if type(price) not in {float, int}:
            raise ValueError('price should be float or integer')
        if not isinstance(quantity, int):
            raise ValueError('quantity should be integer')
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.total_price = self.price * self.quantity
        self.all.append(self)

    def __repr__(self):
        """Возвращает строку с названием класса и полями при инизиализации экземпляров класса"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Возвращает строку с названием класса и полями при инизиализации экземпляров класса в дружественном формате"""
        result = f'Класс {self.__class__.__name__}:\n'
        for elem in self.__dict__:
            if elem == '_Item__name':
                result += f'Name = {self.name}\n'
            else:
                result += f'{elem} = {self.__dict__[elem]}\n'
        return result

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str):
            raise ValueError('new name should be string')
        elif len(new_name) < 10:
            self.__name = new_name
        else:
            raise ValueError('length of new name should be not greater 10 symbols')

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Считывает из csv-файла по предложенному пути данные и записывает их в экземпляры класса Item.
        Eсли в файле не 3 элемента в строке, то возбудит исключение ValueError. Если некорректный путь к файлу,
        то вернет строку с оповещением. При записи данных в экземпляр класса с помощью staticmethod string_to_number()
        автоматически данные преобразуются в правильные типа данных, если в файле содержатся объекты, которые
        нельзя преобразовать, то метод вернет оповещающую строку.
        """

        if not os.path.isfile(path):
            raise FileNotFoundError(f"Отсутствует файл {path}")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if len(row) != 3:
                    raise InstantiateCSVError(path)
                if None in row.keys() or None in row.values():
                    raise InstantiateCSVError(path)
                name, price, quantity = row.values()
                try:
                    cls(str(name), cls.string_to_number(price), cls.string_to_number(quantity))
                except (ValueError, AttributeError):
                    return 'Проверьте содержимое файла:' \
                           'name — это строка, price — это integer или float, а quantity — это integer.\n'

    @staticmethod
    def string_to_number(user_str: str):
        """Преобразует integer и float из string"""
        if user_str.isdigit():
            return int(user_str)
        try:
            result = float(user_str)
            return int(result)
        except ValueError:
            return 'user_str должен содержать int или float'

    def __add__(self, other):
        """Складывает количество товаров по полю 'quantity' у экземпляров классов, унаследованных от класса Item"""
        if not issubclass(other.__class__, self.__class__):
            raise ValueError("Операция сложения только между экземплярами классов Item и Phone по полю 'quantity'.")
        return self.quantity + other.quantity

