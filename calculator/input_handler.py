"""
This module provides functions for obtaining user input for arithmetic operations.
"""

from decimal import Decimal

def get_user_input():
    """
    Prompt the user to enter two decimal numbers and return them.

    Returns:
        tuple: A tuple containing two Decimal numbers entered by the user.
    """
    a = Decimal(input("Enter the first number: "))
    b = Decimal(input("Enter the second number: "))
    return a, b
