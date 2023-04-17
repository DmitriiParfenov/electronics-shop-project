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
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_price = self.price * self.quantity

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
