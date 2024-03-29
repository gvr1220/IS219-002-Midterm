import pandas as pd
from decimal import Decimal

class Calculations:
    def __init__(self, file_path='history.csv'):
        self.file_path = file_path
        self.load_history()

    def load_history(self):
        try:
            self.history = pd.read_csv(self.file_path)
        except FileNotFoundError:
            self.history = pd.DataFrame(columns=['Index', 'Operand 1', 'Operand 2', 'Operation', 'Result'])

    def save_history(self):
        self.history.to_csv(self.file_path, index=False)  # Exclude index when saving

    def add_calculation(self, a: Decimal, b: Decimal, operation: str, result: Decimal):
        if self.history.empty:
            new_index = 1
        else:
            new_index = self.history['Index'].max() + 1
        new_calculation = pd.DataFrame([[new_index, a, b, operation, result]], columns=['Index', 'Operand 1', 'Operand 2', 'Operation', 'Result'])
        self.history = pd.concat([self.history, new_calculation], ignore_index=True)
        self.save_history()

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Index', 'Operand 1', 'Operand 2', 'Operation', 'Result'])
        self.save_history()

    def delete_record(self, index: int):
        self.history = self.history.drop(index - 1)
        self.history['Index'] = range(1, len(self.history) + 1)  # Re-indexing
        self.save_history()

    def get_history(self):
        return self.history

    def get_latest(self):
        if not self.history.empty:
            return self.history.iloc[-1]
        else:
            return None
