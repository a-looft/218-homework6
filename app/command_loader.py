import os
import importlib
from app.command_interface import Command

def load_commands():
    commands = {}
    path = os.path.join(os.path.dirname(__file__), "commands")

    for file in os.listdir(path):
        if file.endswith("_command.py"):
            module = importlib.import_module(f"app.commands.{file[:-3]}")
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and issubclass(obj, Command) and obj is not Command:
                    instance = obj()
                    commands[instance.get_name()] = instance
    return commands
