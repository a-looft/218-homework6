# pylint: disable=invalid-name, missing-module-docstring, missing-class-docstring, missing-function-docstring

import sys
from calculator import Calculator 

def main():
    try:
        a = sys.argv[1]
        b = sys.argv[2]
        operation = sys.argv[3]

        if not a.isdigit() or not b.isdigit():
            raise ValueError(f"{a} or {b} is not a valid number.")

        a = int(a)
        b = int(b)

        if operation == 'add':
            result = Calculator.add(a, b)
        elif operation == 'subtract':
            result = Calculator.subtract(a, b)
        elif operation == 'multiply':
            result = Calculator.multiply(a, b)
        elif operation == 'divide':
            try:
                result = Calculator.divide(a, b)
            except ZeroDivisionError:
                print("cannot divide by zero")
                return
        else:
            print(f"unknown operation: {operation}")
            return

        print(f"The result of {a} {operation} {b} is equal to {result}")

    except IndexError:
        print("python main.py <a> <b> <operation>")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
