from app.commands.add_command import AddCommand
from app.commands.subtract_command import SubtractCommand
from app.commands.multiply_command import MultiplyCommand
from app.commands.divide_command import DivideCommand

def test_add_command():
    cmd = AddCommand()
    assert cmd.execute("2", "3") == "5.0"
    assert "Error" in cmd.execute("a", "b")

def test_subtract_command():
    cmd = SubtractCommand()
    assert cmd.execute("5", "3") == "2.0"

def test_multiply_command():
    cmd = MultiplyCommand()
    assert cmd.execute("4", "2") == "8.0"

def test_divide_command():
    cmd = DivideCommand()
    assert cmd.execute("10", "2") == "5.0"
    assert "Error" in cmd.execute("10", "0")
