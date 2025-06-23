from app.command_interface import Command
from app.calculator.calculator import Calculator

class MultiplyCommand(Command):
    def get_name(self):
        return "multiply"

    def execute(self, *args):
        try:
            a, b = float(args[0]), float(args[1])
            return str(Calculator.multiply(a, b))
        except Exception as e:
            return f"Error: {str(e)}"
