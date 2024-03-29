"""
This module provides a class representing a mathematical calculation.
"""

from decimal import Decimal
from typing import Callable

class Calculation:
    """
    This class represents a mathematical calculation.

    Attributes:
        a (Decimal): The first operand of the calculation.
        b (Decimal): The second operand of the calculation.
        operation (Callable[[Decimal, Decimal], Decimal]): The operation to perform on the operands.
    """

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Initialize a Calculation instance.

        Args:
            a (Decimal): The first operand of the calculation.
            b (Decimal): The second operand of the calculation.
            operation: The operation to perform on the operands.
        """
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Create a Calculation instance.

        Args:
            a (Decimal): The first operand of the calculation.
            b (Decimal): The second operand of the calculation.
            operation: The operation to perform on the operands.

        Returns:
            Calculation: A Calculation instance.
        """
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """
        Perform the calculation.

        Returns:
            Decimal: The result of the calculation.
        """
        return self.operation(self.a, self.b)

    def __repr__(self):
        """
        Return a string representation of the Calculation instance.

        Returns:
            str: A string representation of the Calculation instance.
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
