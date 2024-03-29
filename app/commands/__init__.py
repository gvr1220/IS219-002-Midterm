"""
This module defines the Command and CommandHandler classes.
"""

from abc import ABC, abstractmethod
# pylint: disable=too-few-public-methods


class Command(ABC):
    """
    Abstract base class for command objects.
    """

    @abstractmethod
    def execute(self):
        """
        Execute the command.
        """
        pass # pylint: disable=unnecessary-pass


class CommandHandler:
    """
    Class to handle registration and execution of commands.
    """

    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """
        Register a command with the handler.

        Args:
            command_name (str): The name of the command.
            command (Command): The command object.
        """
        self.commands[command_name] = command

    def execute_command(self, command_input: str):
        """Execute a command based on input."""
        try:
            # Attempt to convert input to integer, indicating menu option number
            menu_option = int(command_input)
            if menu_option < 1 or menu_option > len(self.commands):
                print("Invalid menu option. Please enter a valid option number.")
                return
            command_name = list(self.commands.keys())[menu_option - 1]#Get command name from index
        except ValueError:
            # If input cannot be converted to integer, treat it as command name
            command_name = command_input.lower()

        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
