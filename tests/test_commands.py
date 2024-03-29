import unittest
from unittest.mock import patch
from io import StringIO
from app.commands import CommandHandler, Command
from app.commands.operation_command import OperationCommand


class MockCommand(Command):
    def execute(self):
        pass


class TestCommandHandler(unittest.TestCase):
    def setUp(self):
        self.command_handler = CommandHandler()

    def test_register_command(self):
        mock_command = MockCommand()
        self.command_handler.register_command("test_command", mock_command)
        self.assertIn("test_command", self.command_handler.commands)
        self.assertEqual(mock_command, self.command_handler.commands["test_command"])

    def test_execute_command_invalid_menu_option(self):
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            self.command_handler.execute_command("0")
            self.assertEqual(mocked_stdout.getvalue().strip(), "Invalid menu option. Please enter a valid option number.")

    @patch('builtins.input', side_effect=["2", "3"])  # Providing numeric input for add operation
    def test_execute_command_operation(self, mocked_input):
        add_function = lambda a, b: a + b
        add_function.__name__ = "add"  # Set function name for lambda
        self.command_handler.register_command("add", OperationCommand(add_function))
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            self.command_handler.execute_command("add")
            self.assertEqual(mocked_stdout.getvalue().strip(), "The result of add operation is: 5")

