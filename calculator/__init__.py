"""
This module provides a Calculator class for performing arithmetic operations on Decimal numbers.
"""

from decimal import Decimal
from typing import Callable
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:
    """
    A class representing a Calculator for performing arithmetic operations.
    """

    @staticmethod
    def perform_operation(a: Decimal, b: Decimal,
                          operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """
        Perform a calculation and return the result.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.
            operation (Callable[[Decimal, Decimal], Decimal]): The operation to perform.

        Returns:
            Decimal: The result of the calculation.
        """
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """
        Add two Decimal numbers.

        Args:
            a (Decimal): The first number.
            b (Decimal): The second number.

        Returns:
            Decimal: The sum of the two numbers.
        """
        return Calculator.perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """
        Subtract one Decimal number from another.

        Args:
            a (Decimal): The minuend.
            b (Decimal): The subtrahend.

        Returns:
            Decimal: The result of subtracting b from a.
        """
        return Calculator.perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """
        Multiply two Decimal numbers.

        Args:
            a (Decimal): The first number.
            b (Decimal): The second number.

        Returns:
            Decimal: The product of the two numbers.
        """
        return Calculator.perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """
        Divide one Decimal number by another.

        Args:
            a (Decimal): The dividend.
            b (Decimal): The divisor.

        Returns:
            Decimal: The result of dividing a by b.
        """
        return Calculator.perform_operation(a, b, divide)
