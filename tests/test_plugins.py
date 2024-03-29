"""
Module docstring: This module contains unit tests for the App class and its commands.
"""

import unittest
from unittest.mock import patch
from io import StringIO
from app import App
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.menu import MenuCommand
from app.plugins.history import HistoryCommand


@patch('sys.exit')
def test_add_command(mock_exit, capsys):
    """Test the add command."""
    inputs = iter(['10', '20', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("add", AddCommand())
        app.command_handler.execute_command("add")
        captured = capsys.readouterr()
        assert "The result of add operation is: 30" in captured.out
        assert not mock_exit.called  # Ensure sys.exit was not called


def test_subtract_command(capsys):
    """Test the subtract command."""
    inputs = iter(['20', '5', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("subtract", SubtractCommand())
        app.command_handler.execute_command("subtract")
        captured = capsys.readouterr()
        assert "The result of subtract operation is: 15" in captured.out


def test_multiply_command(capsys):
    """Test the multiply command."""
    inputs = iter(['10', '3', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("multiply", MultiplyCommand())
        app.command_handler.execute_command("multiply")
        captured = capsys.readouterr()
        assert "The result of multiply operation is: 30" in captured.out


def test_divide_command(capsys):
    """Test the divide command."""
    # Test division with non-zero divisor
    inputs = iter(['20', '4', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("divide", DivideCommand())
        app.command_handler.execute_command("divide")
        captured = capsys.readouterr()
        assert "The result of divide operation is: 5" in captured.out

    # Test division with zero divisor
    inputs = iter(['20', '0', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("divide", DivideCommand())
        app.command_handler.execute_command("divide")
        captured = capsys.readouterr()
        assert "Cannot divide by zero" in captured.out


def test_menu_command(capsys):
    """Test the menu command."""
    with patch('builtins.input', side_effect=['exit']):
        app = App()
        app.command_handler.register_command("menu", MenuCommand())
        app.command_handler.execute_command("menu")
        captured = capsys.readouterr()
        assert "Menu:" in captured.out
        assert "1. add" in captured.out
        assert "2. subtract" in captured.out
        assert "3. multiply" in captured.out
        assert "4. divide" in captured.out
        assert "5. history" in captured.out

class TestHistoryCommand(unittest.TestCase):

    @patch('app.plugins.history.HistoryCommand.show_history')
    @patch('builtins.input', side_effect=['1', '4'])
    def test_execute_show_history(self, mock_input, mock_show_history):
        command = HistoryCommand()
        command.execute()
        mock_show_history.assert_called()

    @patch('app.plugins.history.HistoryCommand.clear_history')
    @patch('builtins.input', side_effect=['2', '4'])
    def test_execute_clear_history(self, mock_input, mock_clear_history):
        command = HistoryCommand()
        command.execute()
        mock_clear_history.assert_called()

    @patch('app.plugins.history.HistoryCommand.delete_record')
    @patch('builtins.input', side_effect=['3', '4'])
    def test_execute_delete_record(self, mock_input, mock_delete_record):
        command = HistoryCommand()
        command.execute()
        mock_delete_record.assert_called()

    @patch('builtins.input', side_effect=['4'])
    def test_execute_exit(self, mock_input):
        command = HistoryCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            command.execute()
            self.assertEqual(mock_stdout.getvalue().strip(), 'History Menu:\n1. Show History\n2. Clear History\n3. Delete Record\n4. Return to Main Menu')

    @patch('app.plugins.history.Calculations.clear_history')
    def test_clear_history(self, mock_clear_history):
        command = HistoryCommand()
        command.clear_history()
        mock_clear_history.assert_called()

    @patch('builtins.input', return_value='1')
    @patch('app.plugins.history.Calculations.delete_record')
    def test_delete_record(self, mock_delete_record, mock_input):
        command = HistoryCommand()
        command.delete_record()
        mock_delete_record.assert_called_with(1)

