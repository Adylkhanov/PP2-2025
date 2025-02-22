import re

def snake_camel(s):

    pattern =r"_([a-z])"

    s = re.sub(pattern, lambda match: match.group(1).upper(), s)


    return s

print(snake_camel(input()))
