import re

def find_seq(s):
    pattern = r'\b[a-z]+(?:_[a-z]+)+\b'
    return re.search(pattern, s)


print(find_seq("applebanana_true"))
