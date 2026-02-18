from app.calculator.calculator import Calculator


def test_calculator_add():
    assert Calculator.calculate(10, 5, "add") == 15


def test_calculator_multiply():
    assert Calculator.calculate(6, 7, "multiply") == 42
