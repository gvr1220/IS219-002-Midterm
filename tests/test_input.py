import unittest
from unittest.mock import patch
from calculator.input_handler import get_user_input

class TestInputHandler(unittest.TestCase):
    @patch('builtins.input', side_effect=['10', '20'])
    def test_get_user_input_valid(self, mock_input):
        a, b = get_user_input()
        self.assertEqual(a, 10)
        self.assertEqual(b, 20)

    @patch('builtins.input', side_effect=['abc', '20', 'yes'])
    def test_get_user_input_invalid_then_valid(self, mock_input):
        with self.assertLogs('root', level='WARNING') as log:
            a, b = get_user_input()
            self.assertIsNone(a)
            self.assertIsNone(b)
            self.assertIn('Invalid input detected', log.output[0])

    @patch('builtins.input', side_effect=['10', 'abc', 'no'])
    def test_get_user_input_valid_then_invalid(self, mock_input):
        with self.assertLogs('root', level='WARNING') as log:
            a, b = get_user_input()
            self.assertIsNone(a)
            self.assertIsNone(b)
            self.assertIn('Invalid input detected', log.output[0])


