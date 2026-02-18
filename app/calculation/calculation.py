class Calculation:
    """Represents a calculation with two operands and an operation"""

    def __init__(self, a: float, b: float, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> float:
        return self.operation.calculate(self.a, self.b)
