def map(array, lens):
    """Apply the lens function to all elements in an array"""
    return [lens(n) for n in array]

def cipher(message, key):
    return ''.join(map(message, lambda x: chr(ord(x) + key)))

""" Test Cases """
print(map([1, 2, 3, 4, 5], lambda x: x * 2))
print(cipher("hello", -3))
