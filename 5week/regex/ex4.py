import re

def ex4func(s):
    pattern = r'\b[A-Z][a-z]+\b'
    return re.findall(pattern, s)

print(ex4func(input()))