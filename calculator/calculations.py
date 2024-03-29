""""
Module for performing calculations and managing calculation history.
"""
from decimal import Decimal
import pandas as pd

class Calculations:
    """
    Class for performing calculations and managing calculation history.
    """
    def __init__(self, file_path='history.csv'):
        """
        Initialize Calculations object.
        """
        self.file_path = file_path
        self.history = pd.DataFrame(columns=['Index', 'Operand 1',
                                             'Operand 2', 'Operation', 'Result'])
        self.load_history()

    def load_history(self):
        """
        Load calculation history from a CSV file.
        If the file doesn't exist, initialize an empty DataFrame.
        """
        try:
            self.history = pd.read_csv(self.file_path)
        except FileNotFoundError:
            self.save_history()  # Create an empty history file
        except Exception as e:
            print(f"Error loading history: {e}")

    def save_history(self):
        """
        Save calculation history to a CSV file.
        """
        self.history.to_csv(self.file_path, index=False)  # Exclude index when saving

    def add_calculation(self, a: Decimal, b: Decimal, operation: str, result: Decimal):
        """
        Add a calculation record to the history.
        """
        new_index = len(self.history) + 1
        new_calculation = pd.DataFrame([[new_index, a, b, operation, result]],
                                       columns=['Index', 'Operand 1', 'Operand 2',
                                                'Operation', 'Result'])
        self.history = pd.concat([self.history, new_calculation], ignore_index=True)
        self.save_history()

    def clear_history(self):
        """
        Clear the calculation history.
        """
        self.history = pd.DataFrame(columns=['Index', 'Operand 1',
                                             'Operand 2', 'Operation', 'Result'])
        self.save_history()

    def delete_record(self, index: int):
        """
        Delete a record from the calculation history.
        """
        self.history = self.history.drop(index - 1)
        self.history['Index'] = range(1, len(self.history) + 1)  # Re-indexing
        self.save_history()

    def get_history(self):
        """
        Retrieve the calculation history.
        """
        return self.history

    def get_latest(self):
        """
        Get the latest calculation record from the history.
        """
        if not self.history.empty:
            return self.history.iloc[-1]
        return None

