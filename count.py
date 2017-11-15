def length(n):
    """Count characters in a string."""
    _length = 0
    for i in n: _length += 1
    return _length

""" Test Cases """
print(length("John Appleseed"))
print(length("Supercalifragilisticexpialidocious"))
