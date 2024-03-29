"""
This module defines the OperationCommand class.
"""

import logging
from app.commands import Command
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.input_handler import get_user_input

operation_symbols = {
    'add': '+',
    'subtract': '-',
    'multiply': '*',
    'divide': '/',
}
class OperationCommand(Command):
    def __init__(self, operation_function):
        super().__init__()
        self.operation_function = operation_function
        self.loggers = logging.getLogger()

    def execute(self):
        a, b = get_user_input()
        if a is None or b is None:  # Check if operands are None
            print("Returning to main page...")
            self.loggers.info("User chose to return to the main page")
            return  # Return to main page
        try:
            result = self.operation_function(a, b)
            calculation = Calculation.create(a, b, self.operation_function)
            operation_name = self.operation_function.__name__
            operation_symbol = operation_symbols.get(operation_name, '')
            log_message = f"{operation_name} operation, {a} {operation_symbol} {b} = {result}"
            print(f"The result of {operation_name} operation is: {result}")
            self.loggers.info(log_message)
        except ValueError as e:
            self.loggers.error(str(e))
            print(e)