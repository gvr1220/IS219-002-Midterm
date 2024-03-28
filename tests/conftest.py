"""
This module provides functions for generating test data and running tests for calculator operations.
"""
# pylint: disable=comparison-with-callable
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    """
    Generate test data for calculator operations.

    Args:
        num_records (int): Number of test records to generate.

    Yields:
        tuple: A tuple containing operands, operation name, operation function, and expected result.
    """
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 \
            else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(
            elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        if operation_func == divide:
            b = Decimal('1') if b == Decimal('0') else b

        try:
            if operation_func == divide and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """
    Add command-line option for number of test records.
    """
    parser.addoption("--num_records", action="store",
                     default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """
    Generate test cases using pytest metafunc.
    """
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [
            (a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
            for a, b, op_name, op_func, expected in parameters
        ]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)