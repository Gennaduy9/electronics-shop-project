import pytest
from src.phone import Phone


@pytest.fixture
def phone_x():
   return Phone('iPhone 15', 112000, 3, 3)


def test_setter(phone_x):
    assert phone_x.number_of_sim == 3
    assert str(phone_x) == 'iPhone 15'
    assert repr(phone_x) == "Phone('iPhone 15', 112000, 3, 3)"
    assert phone_x.number_of_sim == 3