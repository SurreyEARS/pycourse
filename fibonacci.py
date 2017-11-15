def fibonacci(n):
    """Well, this one's self-explanatory."""
    _fibonacci = [0, 1, 1]
    for i in range(3, n):
        _next = _fibonacci[i - 1] + _fibonacci[i - 2]
        _fibonacci.append(_next)
    return _fibonacci

def recursive(n):
    """Well, this one's self-explanatory."""
    if n == 1: return [0]
    elif n == 2: return [0, 1]
    elif n == 3: return [0, 1, 1]
    _tail = recursive(n - 1)
    return _tail + [_tail[-1] + _tail[-2]]

""" Test Cases """
print(fibonacci(5))
print(recursive(5))

print(fibonacci(15))
print(recursive(15))
