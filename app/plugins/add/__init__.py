"""
This module defines the AddCommand class.
"""

import logging
from app.commands.operation_command import OperationCommand
from calculator.operations import add
# pylint: disable=too-few-public-methods


class AddCommand(OperationCommand):
    """
    Represents a command for performing addition operations.
    """

    def __init__(self):
        super().__init__(add)
        self.logger = logging.getLogger(__name__)
