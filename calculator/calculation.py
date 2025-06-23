# pylint: disable=invalid-name, missing-module-docstring, missing-class-docstring, missing-function-docstring

from typing import Callable

class Calculation:
    def __init__(self, a: float, b: float, operation: Callable[[float, float], float]):
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self) -> float:
        return self.operation(self.a, self.b)
