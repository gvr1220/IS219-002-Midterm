import unittest
from calculator import Calculations
from decimal import Decimal
import os

class TestCalculations(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculations(file_path='test_history.csv')

    def tearDown(self):
        if os.path.exists('test_history.csv'):
            os.remove('test_history.csv')

    def test_add_calculation(self):
        self.calculator.add_calculation(Decimal('2'), Decimal('3'), 'add', Decimal('5'))
        history = self.calculator.get_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history['Operand 1'].iloc[0], Decimal('2'))
        self.assertEqual(history['Operand 2'].iloc[0], Decimal('3'))
        self.assertEqual(history['Operation'].iloc[0], 'add')
        self.assertEqual(history['Result'].iloc[0], Decimal('5'))

    def test_delete_record(self):
        self.calculator.add_calculation(Decimal('2'), Decimal('3'), 'add', Decimal('5'))
        self.calculator.delete_record(1)
        history = self.calculator.get_history()
        self.assertEqual(len(history), 0)

    def test_clear_history(self):
        self.calculator.add_calculation(Decimal('2'), Decimal('3'), 'add', Decimal('5'))
        self.calculator.clear_history()
        history = self.calculator.get_history()
        self.assertEqual(len(history), 0)

    def test_get_latest(self):
        self.assertIsNone(self.calculator.get_latest())
        self.calculator.add_calculation(Decimal('2'), Decimal('3'), 'add', Decimal('5'))
        latest = self.calculator.get_latest()
        self.assertIsNotNone(latest)
        self.assertEqual(latest['Operand 1'], Decimal('2'))
        self.assertEqual(latest['Operand 2'], Decimal('3'))
        self.assertEqual(latest['Operation'], 'add')
        self.assertEqual(latest['Result'], Decimal('5'))

    def test_invalid_delete_record(self):
        self.assertEqual(len(self.calculator.get_history()), 0)
        with self.assertRaises(KeyError):
            self.calculator.delete_record(1)
        self.calculator.add_calculation(Decimal('2'), Decimal('3'), 'add', Decimal('5'))
        with self.assertRaises(KeyError):
            self.calculator.delete_record(2)

if __name__ == '__main__':
    unittest.main()
