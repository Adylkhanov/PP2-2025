import re

def replaces(s):
    pattern = r"[., ]"

    return re.sub(pattern, ':', s)


print(replaces(input()))
print(replaces("Hellow, World !"))