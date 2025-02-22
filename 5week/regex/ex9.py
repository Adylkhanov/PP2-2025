import re

def uppercase(s):
    pattern = r"[A-Z][a-z]*"
    s = re.findall(pattern, s)
    s = " ".join(s)

    return s


print(uppercase(input()))
