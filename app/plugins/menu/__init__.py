"""
This module provides the MenuCommand class for displaying a menu of options.
"""
from app.commands import Command


class MenuCommand(Command):
    """
    Represents a command for displaying a menu of options.
    """
    def execute(self):
        menu_options = [
            "add",
            "subtract",
            "multiply",
            "divide"
        ]
        print("Menu:")
        for index, option in enumerate(menu_options, start=1):
            print(f"{index}. {option}")
