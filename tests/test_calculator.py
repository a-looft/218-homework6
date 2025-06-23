# pylint: disable=invalid-name, missing-module-docstring, missing-class-docstring, missing-function-docstring

from faker import Faker
import pytest
from calculator.calculation import Calculation
from calculator.calculator import Calculator


fake = Faker()


@pytest.fixture
def sample_data():
    return [
        (1, 2, 3),  # add
        (5, 3, 2),  # subtract
        (4, 2, 8),  # multiply
        (10, 2, 5), # divide
    ]


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 5, 5)
])
def test_add(a, b, expected):
    assert Calculator.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (0, 0, 0),
    (-1, -1, 0)
])
def test_subtract(a, b, expected):
    assert Calculator.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (0, 10, 0),
    (-2, 4, -8)
])
def test_multiply(a, b, expected):
    assert Calculator.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3)
])


def test_divide(a, b, expected):
    assert Calculator.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)


def test_add_calculation_and_get_last():
    Calculator.clear_history()
    calc = Calculation(2, 3, Calculator.add)
    Calculator.add_calculation(calc)
    result = Calculator.get_last_calculation().get_result()
    assert result == 5


def test_clear_history():
    calc = Calculation(1, 1, Calculator.add)
    Calculator.add_calculation(calc)
    Calculator.clear_history()
    assert len(Calculator.history) == 0


def test_fake_add():
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    result = Calculator.add(a, b)
    assert result == a + b


def test_generated_data(a_b_op_expected):
    a, b, op, expected = a_b_op_expected

    if op == 'add':
        assert Calculator.add(a, b) == expected
    elif op == 'subtract':
        assert Calculator.subtract(a, b) == expected
    elif op == 'multiply':
        assert Calculator.multiply(a, b) == expected
    elif op == 'divide':
        if b != 0:
            assert Calculator.divide(a, b) == expected
        else:
            with pytest.raises(ZeroDivisionError):
                Calculator.divide(a, b)
