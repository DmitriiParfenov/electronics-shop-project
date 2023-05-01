from typing import Union

from src.item import Item


class Phone(Item):
    """Класс для представления информации о телефонах с дополнительной информацией о количестве SIM-карт"""

    def __init__(self, name: str, price: Union[int, float], quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone(Item).

        :param name: Название товара, унаследовано от Item.
        :param price: Цена за единицу товара, унаследовано от Item.
        :param quantity: Количество товара в магазине, унаследовано от Item.
        :param number_of_sim: Количество SIM-карт.
        """
        super().__init__(name, price, quantity)
        if not isinstance(number_of_sim, int):
            raise ValueError("Количество SIM-карт должно определяться целым числом.")
        if number_of_sim <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        if value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value

    def __repr__(self):
        """Возвращает строку с названием класса и полями при инизиализации экземпляров класса"""
        return super().__repr__()[:-1] + f', {self.__number_of_sim})'

    def __str__(self):
        """Возвращает строку с названием класса и полями при инизиализации экземпляров класса в дружественном формате"""
        result = ''
        list_attrs = super().__str__().split('\n')
        for elem in list_attrs:
            if not elem.startswith('_'):
                result += f'{elem}\n'
        result = result.strip() + f'\nSIM-card quantity = {self.__number_of_sim}\n'
        return result
