"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def item_shop():
    return Item('видеокамера',1000, 20)


def test_positive_shop_init(item_shop):
    """Когда мы создаем экземпляр класса item, возращаем name, quantity, price"""
    assert item_shop.name == 'видеокамера'
    assert item_shop.quantity == 20
    assert item_shop.price == 1000


def test_calculate_total_price(item_shop):
    """Когда мы создаем класс со значением Х, затем вызываем calculate_total_price, то item_shop вернет нам Х * 1."""
    item_shop.calculate_total_price()
    assert item_shop


def test_apply_discount(item_shop):
    """Когда мы создаем экземпляр класса со скидкой, вернется скидка."""
    Item.pay_rate = 0.5
    item_shop.apply_discount()
    assert item_shop.price == 500

def test_name_setter(item_shop):
    Item.name = "Клавиатура"
    assert Item.name == "Клавиатура"

def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert items.name == "Клавиатура"
    assert items.price == 75
    assert items.quantity == 5


def test_string_to_number():
    assert Item.string_to_number('5,55') == 5.55
    assert Item.string_to_number('10,00') == 10.0
    assert Item.string_to_number('0,99') == 0.99
    assert Item.string_to_number('100') == 100.0









