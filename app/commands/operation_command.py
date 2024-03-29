"""
This module defines the OperationCommand class.
"""

import logging
from app.commands import Command
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.input_handler import get_user_input


class OperationCommand(Command):
    """
    Represents a command for performing arithmetic operations.
    """

    def __init__(self, operation_function):
        super().__init__()
        self.operation_function = operation_function
        self.loggers = logging.getLogger(__name__)

    def execute(self):
        """
        Execute the operation command.
        """
        a, b = get_user_input()
        try:
            result = self.operation_function(a, b)
            calculation = Calculation.create(a, b, self.operation_function)
            Calculations.add_calculation(calculation)
            self.loggers.info("%s operation, result = %s", self.operation_function.__name__, result)
            print(f"The result of {self.operation_function.__name__} operation is {result}")
        except ValueError as e:
            self.loggers.error(str(e))
            print(e)
            print("Please enter a non-zero divisor.")
