from app.commands import Command

class MenuCommand(Command):
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