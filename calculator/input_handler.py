"""
This module contains functions for getting user input and logging warnings.
"""
import logging
from decimal import Decimal, InvalidOperation

logging.basicConfig(level=logging.INFO)
loggers = logging.getLogger("root")


def get_user_input():
    """Get user input for two decimal numbers.

    Returns:
    Tuple[Decimal, Decimal]: A tuple containing two Decimal numbers entered by the user.
    """
    while True:
        try:
            a = Decimal(input("Enter the first number: "))
            b = Decimal(input("Enter the second number: "))
            return a, b
        except InvalidOperation:
            print("Invalid input! Please enter a valid number.")
            loggers.warning("Invalid input detected")
            choice = input("Do you want to continue? (yes/no): ").lower()
            if choice != 'yes':
                return None, None  #user wants to return to the main page