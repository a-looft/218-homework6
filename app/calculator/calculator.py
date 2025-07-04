# pylint: disable=invalid-name, missing-module-docstring, missing-class-docstring, missing-function-docstring

from typing import List
from .calculation import Calculation

class Calculator:
    history: List[Calculation] = []


    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        return cls.history[-1]

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()


    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
