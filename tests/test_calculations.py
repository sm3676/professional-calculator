import pytest
from app.calculation.calculation_factory import CalculationFactory


def test_factory_add():
    calc = CalculationFactory.create_calculation(2, 3, "add")
    assert calc.perform() == 5


def test_factory_subtract():
    calc = CalculationFactory.create_calculation(5, 2, "subtract")
    assert calc.perform() == 3


def test_factory_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create_calculation(1, 1, "invalid")
