"""
Module docstring: This module contains unit tests for the App class and its commands.
"""

from unittest.mock import patch
from app import App
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.menu import MenuCommand


@patch('sys.exit')
def test_add_command(mock_exit, capsys):
    """Test the add command."""
    inputs = iter(['10', '20', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("add", AddCommand())
        app.command_handler.execute_command("add")
        captured = capsys.readouterr()
        assert "The result of add operation is 30" in captured.out
        assert not mock_exit.called  # Ensure sys.exit was not called


def test_subtract_command(capsys):
    """Test the subtract command."""
    inputs = iter(['20', '5', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("subtract", SubtractCommand())
        app.command_handler.execute_command("subtract")
        captured = capsys.readouterr()
        assert "The result of subtract operation is 15" in captured.out


def test_multiply_command(capsys):
    """Test the multiply command."""
    inputs = iter(['10', '3', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("multiply", MultiplyCommand())
        app.command_handler.execute_command("multiply")
        captured = capsys.readouterr()
        assert "The result of multiply operation is 30" in captured.out


def test_divide_command(capsys):
    """Test the divide command."""
    # Test division with non-zero divisor
    inputs = iter(['20', '4', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("divide", DivideCommand())
        app.command_handler.execute_command("divide")
        captured = capsys.readouterr()
        assert "The result of divide operation is 5" in captured.out

    # Test division with zero divisor
    inputs = iter(['20', '0', 'exit'])
    with patch('builtins.input', side_effect=inputs):
        app = App()
        app.command_handler.register_command("divide", DivideCommand())
        app.command_handler.execute_command("divide")
        captured = capsys.readouterr()
        assert "Please enter a non-zero divisor." in captured.out


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
