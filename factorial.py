def factorial(n):
    """Determine the factorial of a given number n."""
    _factorial = 1
    for i in range(1, n + 1): _factorial *= i
    return _factorial

def recursive(n):
    """Determine the factorial of a given number n."""
    if n < 2: return 1
    return n * recursive(n - 1)

""" Test Cases """
print(factorial(5))
print(recursive(5))

print(factorial(19))
print(recursive(19))
