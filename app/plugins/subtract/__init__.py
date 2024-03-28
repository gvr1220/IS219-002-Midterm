from app.commands.operation_command import OperationCommand
from calculator.operations import subtract
import logging
class SubtractCommand(OperationCommand):
    def __init__(self):
        super().__init__(subtract)
        self.logger = logging.getLogger(__name__)