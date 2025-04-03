"""
Core calculator operations (A1-A4)
"""
def add(a: float, b: float) -> float:
    """Addition (A1)"""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtraction (A2)"""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplication (A3)"""
    return a * b

def divide(a: float, b: float) -> float:
    """Division (A4)"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print(add(2, 3))