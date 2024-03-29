"""
Unit tests for the input handler module.
"""
import unittest
from unittest.mock import patch
from calculator.input_handler import get_user_input


class TestInputHandler(unittest.TestCase):
    """Test cases for the input handler module."""
    @patch('builtins.input', side_effect=['10', '20'])
    def test_get_user_input_valid(self, _):
        """Test getting user input with valid values."""
        a, b = get_user_input()
        self.assertEqual(a, 10)
        self.assertEqual(b, 20)

    @patch('builtins.input', side_effect=['abc', '20', 'yes'])
    def test_get_user_input_invalid_then_valid(self, _):
        """Test getting user input with invalid value followed by valid value."""
        with self.assertLogs('root', level='WARNING') as log:
            a, b = get_user_input()
            self.assertIsNone(a)
            self.assertIsNone(b)
            self.assertIn('Invalid input detected', log.output[0])

    @patch('builtins.input', side_effect=['10', 'abc', 'no'])
    def test_get_user_input_valid_then_invalid(self, _):
        """Test getting user input with valid value followed by invalid value."""
        with self.assertLogs('root', level='WARNING') as log:
            a, b = get_user_input()
            self.assertIsNone(a)
            self.assertIsNone(b)
            self.assertIn('Invalid input detected', log.output[0])
