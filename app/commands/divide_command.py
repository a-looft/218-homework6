from app.command_interface import Command
from app.calculator.calculator import Calculator

class DivideCommand(Command):
    def get_name(self):
        return "divide"

    def execute(self, *args):
        try:
            a, b = float(args[0]), float(args[1])
            return str(Calculator.divide(a, b))
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"
        except Exception as e:
            return f"Error: {str(e)}"
