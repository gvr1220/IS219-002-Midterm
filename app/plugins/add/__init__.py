from app.commands.operation_command import OperationCommand
from calculator.operations import add
import logging

class AddCommand(OperationCommand):
    def __init__(self):
        super().__init__(add)
        self.logger = logging.getLogger(__name__)
