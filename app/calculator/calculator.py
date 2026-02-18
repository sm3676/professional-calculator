from app.calculation.calculation_factory import CalculationFactory


class Calculator:
    """Main calculator class"""

    @staticmethod
    def calculate(a: float, b: float, operation_type: str) -> float:
        calculation = CalculationFactory.create_calculation(a, b, operation_type)
        return calculation.perform()