"""
This module provides basic arithmetic operations for decimal numbers.
"""

from decimal import Decimal


def add(a: Decimal, b: Decimal) -> Decimal:
    """
    Adds two decimal numbers.

    Args:
        a (Decimal): The first number.
        b (Decimal): The second number.

    Returns:
        Decimal: The sum of the two numbers.
    """
    return a + b


def subtract(a: Decimal, b: Decimal) -> Decimal:
    """
    Subtracts one decimal number from another.

    Args:
        a (Decimal): The minuend.
        b (Decimal): The subtrahend.

    Returns:
        Decimal: The result of subtracting b from a.
    """
    return a - b


def multiply(a: Decimal, b: Decimal) -> Decimal:
    """
    Multiplies two decimal numbers.

    Args:
        a (Decimal): The first number.
        b (Decimal): The second number.

    Returns:
        Decimal: The product of the two numbers.
    """
    return a * b


def divide(a: Decimal, b: Decimal) -> Decimal:
    """
    Divides one decimal number by another.

    Args:
        a (Decimal): The dividend.
        b (Decimal): The divisor.

    Returns:
        Decimal: The result of dividing a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
