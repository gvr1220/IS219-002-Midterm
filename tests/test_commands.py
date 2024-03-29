"""
Unit tests for the commands.
"""
import unittest
from unittest.mock import patch
from io import StringIO
from app.commands import CommandHandler, Command
# pylint: disable=too-few-public-methods


class MockCommand(Command):
    """Mock command class for testing."""
    def execute(self):
        """Mock execute method."""
        pass # pylint: disable=unnecessary-pass

class TestCommandHandler(unittest.TestCase):
    """Test case for CommandHandler class."""
    def setUp(self):
        """Set up test environment."""
        self.command_handler = CommandHandler()

    def test_register_command(self):
        """Test registering a command."""
        mock_command = MockCommand()
        self.command_handler.register_command("test_command", mock_command)
        self.assertIn("test_command", self.command_handler.commands)
        self.assertEqual(mock_command, self.command_handler.commands["test_command"])

    def test_execute_command_invalid_menu_option(self):
        """Test executing a command with an invalid menu option."""
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            self.command_handler.execute_command("0")
            self.assertEqual(mocked_stdout.getvalue().strip(),
                             "Invalid menu option. Please enter a valid option number.")
