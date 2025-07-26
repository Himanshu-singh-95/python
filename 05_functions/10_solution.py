# Recursive Functions 

def factorial(n):
    """Calculate factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Usage
print(factorial(5))  # Output: 120