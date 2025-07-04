# pylint: disable=invalid-name, missing-module-docstring, missing-class-docstring, missing-function-docstring, disable=possibly-used-before-assignment

import pytest
import random
from faker import Faker
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

fake = Faker()

def pytest_addoption(parser):
    parser.addoption(
        "--num_records",
        action="store",
        default=0,
        type=int,
        help="number of test records to generate"
    )

def generate_test_data():
    operations = ['add', 'subtract', 'multiply', 'divide']
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    op = random.choice(operations)
    if op == 'add':
        expected = a + b
    elif op == 'subtract':
        expected = a - b
    elif op == 'multiply':
        expected = a * b
    elif op == 'divide':
        expected = 'ZeroDivisionError' if b == 0 else a / b
    return (a, b, op, expected)

def pytest_generate_tests(metafunc):
    num_records = int(metafunc.config.getoption("num_records"))
    if "a_b_op_expected" in metafunc.fixturenames and num_records > 0:
        test_data = [generate_test_data() for _ in range(num_records)]
        metafunc.parametrize("a_b_op_expected", test_data)

@pytest.fixture
def a_b_op_expected():
    fake = Faker()
    a = fake.random_int(min=0, max=100)
    b = fake.random_int(min=1, max=100)
    op = random.choice(["+", "-", "*", "/"])
    if op == "+":
        expected = a + b
    elif op == "-":
        expected = a - b
    elif op == "*":
        expected = a * b
    else:
        expected = a / b
    return a, b, op, expected
    