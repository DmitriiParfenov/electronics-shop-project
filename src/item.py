import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        if not isinstance(name, str):
            raise ValueError('name should be string')
        if type(price) not in [float, int]:
            raise ValueError('price should be float or integer')
        if not isinstance(quantity, int):
            raise ValueError('quantity should be integer')
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.total_price = self.price * self.quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
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
        нельзя преобразовать, то метод вернут оповещающую строку.
        """
        way = os.path.join(path)
        try:
            with open(way) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) != 3:
                        raise ValueError('проверьте корректность данных в файле')
                    name, price, quantity = row.values()
                    try:
                        Item(str(name), Item.string_to_number(price), Item.string_to_number(quantity))
                    except ValueError:
                        return 'Проверьте содержимое файла:' \
                               'name — это строка, price — это integer или float, а quantity — это integer.\n'
        except FileNotFoundError:
            return f'Файл не найден. Файл с данными должен находиться в scr/'

    @staticmethod
    def string_to_number(user_str):
        """Преобразует integer и float из string"""
        if user_str.isdigit():
            return int(user_str)
        try:
            result = float(user_str)
            return int(result)
        except ValueError:
            return 'user_str должен содержать int или float'
