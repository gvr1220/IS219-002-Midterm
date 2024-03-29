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

    def execute_command(self, command_name: str):
        """
        Easier to ask for forgiveness than permission (EAFP) -
        Use when its going to most likely work"""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
