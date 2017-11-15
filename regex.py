import re

def surrey(email):
    """Determine whether a given string is a valid surrey student email xx00000@surrey.ac.uk."""
    regex = r"[a-zA-Z]{2}[0-9]{5}@surrey\.ac\.uk"
    return bool(re.match(regex,email))

""" Test Cases """
print(surrey("theodore@messinezis.com"))
print(surrey("tm00440@surrey.ac.uk"))
print(surrey("t.messinezis@surrey.ac.uk"))
