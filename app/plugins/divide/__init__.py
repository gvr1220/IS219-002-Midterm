"""
This module defines the DivideCommand class.
"""
import logging
from app.commands.operation_command import OperationCommand
from calculator.operations import divide
# pylint: disable=too-few-public-methods


class DivideCommand(OperationCommand):
    """
    Represents a command for performing division operations.
    """
    def __init__(self):
        super().__init__(divide)
        self.logger = logging.getLogger(__name__)
