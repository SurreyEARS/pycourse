def binary(n):
    """Check if a given integer n is a power of 2"""
    _candidate = 2
    while _candidate <= n:
        if _candidate == n: return True
        _candidate *= 2
    return False

def square(n):
    """Check if a given integer n is a perfect square"""
    _candidate = {"base" : 1, "power" : 1}
    while _candidate["power"] <= n:
        if _candidate["power"] == n: return True
        _candidate["base"] += 1
        _candidate["power"] = _candidate["base"] ** 2
    return False

""" Test Cases """
print(binary(4))
print(square(9))

print(binary(127))
print(binary(128))
print(binary(129))
print(square(48))
print(square(49))
print(square(50))
