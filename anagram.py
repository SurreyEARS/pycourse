def anagram(left, right):
    """Determine whether two strings are anagrams"""
    if len(left) != len(right): return False
    return sorted(left) == sorted(right)

""" Test Cases """
print(anagram("anagram", "nagaram"))
print(anagram("surrey", "ears"))
