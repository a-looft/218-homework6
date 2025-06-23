from app.command_loader import load_commands

def run():
    commands = load_commands()
    print("Homework 5 Calculator")
    print("Type 'menu' to see commands or 'exit' to quit")
    print("Available commands:", ', '.join(commands.keys()))

    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() == "exit":
            break
        if not user_input:
            continue
        if user_input.lower() == "menu":
            print("Available commands:", ', '.join(commands.keys()))
            continue

        parts = user_input.split()
        cmd_name, args = parts[0], parts[1:]

        command = commands.get(cmd_name)
        if not command:
            print(f"Unknown command: '{cmd_name}'")
            continue

        result = command.execute(*args)
        print(result)
