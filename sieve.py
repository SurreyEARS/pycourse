def sieve(n):
    """Sieve of Eratosthenes implementation"""
    _sieve = [True] * (n + 1)
    _sieve[0] = False # The number 0 is not a prime number :/
    _sieve[1] = False # The number 1 is not a prime number :/
    for i in range(2, int(n ** .5 + 1)):
        _candidates = (n for n in range (2 * i, n, i) if _sieve[i])
        for n in _candidates: _sieve[n] = False
    return _sieve

def interface(n):
    """Find the first prime numbers till n using the sieve"""
    _sieve = sieve(n)
    _primes = []
    for i in range(n):
        if _sieve[i]: _primes.append(i)
    return _primes

""" Test Cases """
print(interface(13)) # 13 is actually prime...
print(interface(1000))
