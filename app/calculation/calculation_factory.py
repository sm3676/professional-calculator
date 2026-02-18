from app.operation.add import Add
from app.operation.subtract import Subtract
from app.operation.multiply import Multiply
from app.operation.divide import Divide
from app.calculation.calculation import Calculation


class CalculationFactory:
    """Factory to create Calculation objects based on operation type"""

    operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide
    }

    @staticmethod
    def create_calculation(a: float, b: float, operation_type: str) -> Calculation:
        operation_class = CalculationFactory.operations.get(operation_type.lower())

        if not operation_class:
            raise ValueError("Invalid operation type")

        return Calculation(a, b, operation_class)
