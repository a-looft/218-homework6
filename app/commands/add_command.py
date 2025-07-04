from app.command_interface import Command
from app.calculator.calculator import Calculator

class AddCommand(Command):
    def get_name(self):
        return "add"

    def execute(self, *args):
        try:
            a, b = float(args[0]), float(args[1])
            return str(Calculator.add(a, b))
        except Exception as e:
            return f"Error: {str(e)}"
