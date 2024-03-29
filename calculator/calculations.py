"""
This module provides a class for managing calculations and their history.
"""

from typing import List
from calculator.calculation import Calculation

class Calculations:
    """
    This class manages calculations and their history.
    """

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """
        Add a calculation to the history.

        Args:
            calculation (Calculation): The calculation to add to the history.
        """
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """
        Get the list of all calculations in the history.

        Returns:
            List[Calculation]: A list of Calculation objects representing the history.
        """
        return cls.history

    @classmethod
    def clear_history(cls):
        """
        Clear the history of calculations.
        """
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation | None:
        """
        Get the latest calculation from the history.

        Returns:
            Calculation | None: The latest Calculation object if available, else None.
        """
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """
        Find calculations in the history with a specific operation.

        Args:
            operation_name (str): The name of the operation to search for.

        Returns:
            List[Calculation]: A list of Calculation objects with the specified operation.
        """
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
