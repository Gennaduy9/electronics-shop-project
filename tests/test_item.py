"""Здесь надо написать тесты с использованием pytest для модуля item."""
from unittest.mock import MagicMock

import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone




@pytest.fixture
def item_shop():
    return Item('Видеокамера',1000, 20)


def test_positive_shop_init(item_shop):
    """Когда мы создаем экземпляр класса item, возращаем name, quantity, price"""
    assert item_shop.name == 'Видеокамера'
    assert item_shop.quantity == 20
    assert item_shop.price == 1000


def test_calculate_total_price(item_shop):
    """Когда мы создаем класс со значением Х, затем вызываем calculate_total_price, то item_shop вернет нам Х * 1."""
    item_shop.calculate_total_price()
    assert item_shop


def test_apply_discount(item_shop):
    # """Создаем экземпляр класса со скидкой, вернется скидка."""
    Item.pay_rate = 0.5
    item_shop.apply_discount()
    assert item_shop.price == 500

def test_name_setter(item_shop):
    Item.name = "iPhone 15"
    assert Item.name == "iPhone 15"

def test_string_to_number():
    assert Item.string_to_number('5,55') == 5.55
    assert Item.string_to_number('10,00') == 10.0
    assert Item.string_to_number('0,99') == 0.99
    assert Item.string_to_number('100') == 100.0


def test_magic_method():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


@pytest.fixture
def mocker():
    return MagicMock()

def test_instantiate_from_csv(mocker):
    try:
        items = Item.instantiate_from_csv()
        assert len(items) == 6
        assert items[0].name == 'iPhone 15'
        assert items[0].price == 112000
        assert items[0].quantity == 3
    except FileNotFoundError:
        print('Отсутствует файл item.csv')
    except InstantiateCSVError:
        print('Файл item.csv поврежден')
    finally:
        print('Код в файле item.csv работает корректно')

def test_instantiate_from_csv_valid(mocker):
    mock_file = mocker.mock_open(read_data='name,price,quantity\niPhone 15,112000,3\n')
    with mocker.patch('builtins.open', mock_file):
        items = Item.instantiate_from_csv()
        assert len(items) == 6
        assert items[0].name == 'iPhone 15'
        assert items[0].price == 112000
        assert items[0].quantity == 3

@pytest.fixture
def phone_x():
   return Phone('iPhone 15', 112000, 3, 3)

def test_magic_method_add():
    item_y = Item("Смартфон", 100000, 2)
    assert f'add(item_y) + phone_x == 212000'
    assert f'add(phone_x) + phone_x == 5'


