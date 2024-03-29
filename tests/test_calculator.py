import unittest
from decimal import Decimal
from unittest.mock import patch, MagicMock
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    @patch('calculator.calculations.Calculations.add_calculation')
    def test_add(self, mock_add_calculation):
        mock_add_calculation.return_value = None
        result = Calculator.add(Decimal('5'), Decimal('3'))
        self.assertEqual(result, Decimal('8'))

    @patch('calculator.calculations.Calculations.add_calculation')
    def test_subtract(self, mock_add_calculation):
        mock_add_calculation.return_value = None
        result = Calculator.subtract(Decimal('5'), Decimal('3'))
        self.assertEqual(result, Decimal('2'))

    @patch('calculator.calculations.Calculations.add_calculation')
    def test_multiply(self, mock_add_calculation):
        mock_add_calculation.return_value = None
        result = Calculator.multiply(Decimal('5'), Decimal('3'))
        self.assertEqual(result, Decimal('15'))

    @patch('calculator.calculations.Calculations.add_calculation')
    def test_divide(self, mock_add_calculation):
        mock_add_calculation.return_value = None
        result = Calculator.divide(Decimal('6'), Decimal('2'))
        self.assertEqual(result, Decimal('3'))
