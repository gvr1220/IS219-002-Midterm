"""
implementing the HistoryCommand class for managing calculation history.
"""
import logging
from app.commands import Command
from calculator.calculations import Calculations
# pylint: disable=too-few-public-methods

class HistoryCommand(Command):
    """
    A command class to handle operations related to command history.
    """
    def __init__(self):
        """
        Initializes the HistoryCommand object.
        """
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.calculations = Calculations()

    def execute(self):
        """
        Executes the history command.
        """
        self.logger.info("Executing HistoryCommand")
        while True:
            print("History Menu:")
            print("1. Show History")
            print("2. Clear History")
            print("3. Delete Record")
            print("4. Return to Main Menu")
            choice = input("Enter your number choice: ")
            if choice == '1':
                self.show_history()
            elif choice == '2':
                self.clear_history()
            elif choice == '3':
                self.delete_record()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def show_history(self):
        """
        Displays the command history.
        """
        self.logger.info("Displaying history")
        self.calculations.load_history()  # Reload history from the file
        history = self.calculations.get_history()
        if not history.empty:
            print(history.to_string(index=False))
        else:
            print("History is empty.")

    def clear_history(self):
        """
        Clears the command history.
        """
        self.logger.info("Clearing history")
        self.calculations.clear_history()
        print("History cleared.")

    def delete_record(self):
        """
        Deletes a record from the command history.
        """

        self.logger.info("Deleting record")
        index = int(input("Enter the index of the record to delete: "))
        try:
            self.calculations.delete_record(index)
            print("Record deleted successfully.")
        except IndexError:
            print("Invalid index. Record not found.")
