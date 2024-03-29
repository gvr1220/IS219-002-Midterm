"""
Unit tests for the history commands.
"""
import unittest
from unittest.mock import patch
from io import StringIO
from app.plugins.history import HistoryCommand
class TestHistoryCommand(unittest.TestCase):
    """Unit tests for the history commands."""

    @patch('app.plugins.history.HistoryCommand.show_history')
    @patch('builtins.input', side_effect=['1', '4'])
    def test_show_history(self, _, mock_show_history):
        """Test execute method for showing history."""
        command = HistoryCommand()
        command.execute()
        mock_show_history.assert_called()

    @patch('app.plugins.history.HistoryCommand.clear_history')
    @patch('builtins.input', side_effect=['2', '4'])
    def test_execute_clear_history(self, _, mock_clear_history):
        """Test execute method for clearing history."""
        command = HistoryCommand()
        command.execute()
        mock_clear_history.assert_called()

    @patch('app.plugins.history.HistoryCommand.delete_record')
    @patch('builtins.input', side_effect=['3', '4'])
    def test_execute_delete_record(self, _, mock_delete_record):
        """Test execute method for deleting a record."""
        command = HistoryCommand()
        command.execute()
        mock_delete_record.assert_called()

    @patch('builtins.input', side_effect=['4'])
    def test_exit(self, _):
        """Test execute method for exiting."""
        command = HistoryCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            command.execute()
            self.assertEqual(mock_stdout.getvalue().strip(),
                             'History Menu:\n1. Show History\n'
                             '2. Clear History\n3. Delete Record\n4. Return to Main Menu')

    @patch('app.plugins.history.Calculations.clear_history')
    def test_clear_history(self, mock_clear_history):
        """Test clear_history method."""
        command = HistoryCommand()
        command.clear_history()
        mock_clear_history.assert_called()

    @patch('builtins.input', return_value='1')
    @patch('app.plugins.history.Calculations.delete_record')
    def test_delete_record(self, mock_delete_record, _):
        """Test delete_record method."""
        command = HistoryCommand()
        command.delete_record()
        mock_delete_record.assert_called_with(1)
