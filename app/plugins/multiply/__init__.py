from app.commands.operation_command import OperationCommand
from calculator.operations import multiply
import logging
class MultiplyCommand(OperationCommand):
    def __init__(self):
        super().__init__(multiply)
        self.logger = logging.getLogger(__name__)