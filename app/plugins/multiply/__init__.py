"""
This module defines the MultiplyCommand class.
"""

import logging
from app.commands.operation_command import OperationCommand
from calculator.operations import multiply


class MultiplyCommand(OperationCommand):
    """
    Represents a command for performing multiplication operations.
    """
    def __init__(self):
        super().__init__(multiply)
        self.logger = logging.getLogger(__name__)
