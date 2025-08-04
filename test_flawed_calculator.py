# test_flawed_calculator.py

import pytest
from flawed_calculator import add, subtract, multiply, divide, power

def test_add():
    """Test the addition function (this will pass)."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract_fails():
    """Test the subtraction function (this will fail)."""
    # We expect 5 - 3 to be 2, but the flawed calculator returns 8.
    assert subtract(5, 3) == 2
    # We expect 3 - 5 to be -2, but the flawed calculator returns 8.
    assert subtract(3, 5) == -2

def test_multiply():
    """Test the multiplication function (this will pass)."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5

def test_divide_by_zero_fails():
    """Test that division by zero raises a ValueError (this will fail)."""
    # The flawed calculator does not raise an exception, so this test will fail.
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)
    
def test_divide():
    """Test the division function (this will fail)."""
    # The divide function in flawed_calculator is okay, but this test will still fail
    # because of the `test_divide_by_zero_fails` test.
    assert divide(6, 3) == 2
    assert divide(10, 2) == 5.0