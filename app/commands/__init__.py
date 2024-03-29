"""
This module defines the Command and CommandHandler classes.
"""

from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class for command objects.
    """

    @abstractmethod
    def execute(self):
        """
        Execute the command.
        """
        pass

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

    def execute_command(self, command_name: str):
        """
        Execute a registered command.

        Args:
            command_name (str): The name of the command.
        """
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
