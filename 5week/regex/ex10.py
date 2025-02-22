import re

def uppercase(s):
    pattern = r"[A-Z][a-z]*"
    s = re.findall(pattern, s)

    s = "_".join(s)
    s = str(s)

    return s.lower()


print(uppercase(input()))
