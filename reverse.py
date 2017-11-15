def string(n):
    """Reverse a given string."""
    _reversed = ''
    i = len(n) - 1
    while i >= 0:
        _reversed += n[i]
        i -= 1
    return _reversed

def array(n):
    """Reverse a given list."""
    _reversed = []
    while len(n) > 0: _reversed.append(n.pop())
    return _reversed

""" Test Cases """  
print(string("surreyears"))
print(array([11, 7, 5, 3, 2]))
print(string("O" + "T" + "A" + "T" + "O" + "P"))
print(array([1, 2, 3] + [4, 5, 6]))
