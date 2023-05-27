import pytest
from src.phone import Phone
from src.keyboard import KeyBoard


@pytest.fixture
def phone_x():
    return Phone('iPhone 15', 112000, 3, 3)


def test_setter(phone_x):
    assert phone_x.number_of_sim == 3

def test_change_lang():
    kb = KeyBoard("Клавиатура", 2000, 5)
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    try:
        kb.language = "CH"
    except AttributeError:
        print("EN / RU")

def test_lang_count():
    kb1 = KeyBoard("Клавиатура", 500, 3)
    assert kb1.lang_count == 0
    kb1.change_lang()
    assert kb1.lang_count == 1
    kb1.change_lang()
    assert kb1.lang_count == 2


def test_name():
    kb = KeyBoard("iPhone 15", 112000, 3)
    assert kb.name == "iPhone 15"

def test_price():
    kb = KeyBoard("iPhone 15", 112000, 3)
    assert kb.price == 112000

def test_quantity():
    kb = KeyBoard("iPhone 15", 112000, 3)
    assert kb.quantity == 3
