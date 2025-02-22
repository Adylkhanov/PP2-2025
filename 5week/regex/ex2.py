import re

def match_a_followed_by_two_to_three_bs(s):
    pattern = r'^ab{2,3}$'
    return bool(re.match(pattern, s))

print("")