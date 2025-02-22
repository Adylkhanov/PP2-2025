import re

def uppercase(s):
    pattern = r"[A-Z][a-z]*"
    s = re.findall(pattern, s)


    return s


print(uppercase(input()))
