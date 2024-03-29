"""
This module defines the SubtractCommand class.
"""

import logging
from app.commands.operation_command import OperationCommand
from calculator.operations import subtract
# pylint: disable=too-few-public-methods


class SubtractCommand(OperationCommand):
    """
    Represents a command for performing subtraction operations.
    """

    def __init__(self):
        super().__init__(subtract)
        self.logger = logging.getLogger(__name__)
