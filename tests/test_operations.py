import pytest
from app.operation.add import Add
from app.operation.subtract import Subtract
from app.operation.multiply import Multiply
from app.operation.divide import Divide


def test_add():
    assert Add.calculate(2, 3) == 5


def test_subtract():
    assert Subtract.calculate(5, 3) == 2


def test_multiply():
    assert Multiply.calculate(4, 3) == 12


def test_divide():
    assert Divide.calculate(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Divide.calculate(10, 0)
