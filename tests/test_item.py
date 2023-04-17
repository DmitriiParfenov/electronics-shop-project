import pytest

from src.item import Item


@pytest.fixture
def item_example():
    return Item("Смартфон", 10000, 20)


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

