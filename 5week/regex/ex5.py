import re

def capitl_let(s):
    pattern = r'^a.*b$'

    return re.search(pattern, s)


print(capitl_let(input()))
