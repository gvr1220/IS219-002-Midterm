"""
This module provides the MenuCommand class for displaying a menu of options.
"""
from app.commands import Command
# pylint: disable=too-few-public-methods


class MenuCommand(Command):
    """
    Represents a command for displaying a menu of options.
    """
class MenuCommand(Command):
    """
    Represents a command for displaying a menu of options.
    """
    def execute(self):
        menu_options = [
            "add",
            "subtract",
            "multiply",
            "divide",
            "history",
        ]
        print("Menu:")
        for option in menu_options:
            print(f"- {option}")
