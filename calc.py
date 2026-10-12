# Core application arithmetic module with embedded assertion testing
# Student: Sharma Shubh (4NI25CS191)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    assert add(2, 3) == 5, "Addition test failed"
    assert multiply(3, 4) == 12, "Multiplication test failed"
    assert subtract(10, 4) == 6, "Subtraction test failed"
    assert divide(8, 2) == 4, "Division test failed"
    print("All CI unit test assertions executed successfully!")
