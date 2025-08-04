# test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide, power
def test_add():
    """Test the addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(100, 200) == 300
    assert add(2.5, 3.5) == 6.0

def test_subtract():
    """Test the subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(10, 10) == 0
    assert subtract(0, 5) == -5
    assert subtract(-5, -3) == -2
    assert subtract(5.5, 2.5) == 3.0

def test_multiply():
    """Test the multiplication function."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(-2, -3) == 6
    assert multiply(0, 10) == 0
    assert multiply(10, 0) == 0
    assert multiply(2.5, 2) == 5.0

def test_divide():
    """Test the division function."""
    assert divide(6, 3) == 2
    assert divide(10, 2) == 5.0
    assert divide(-10, 2) == -5.0
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    """Test that division by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)

def test_power():
    """Test the power function."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(10, 1) == 10
    assert power(4, 0.5) == 2.0
    assert power(-2, 2) == 4
    assert power(2, -1) == 0.5