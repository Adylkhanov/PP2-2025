import re


def match_a_followed_by_zero_or_more_bs(s):
    pattern = r'^ab*$'
    return bool(re.match(pattern, s))


print(match_a_followed_by_zero_or_more_bs("abbb"))
print(match_a_followed_by_zero_or_more_bs("baa"))
print(match_a_followed_by_zero_or_more_bs("aabb"))
print(match_a_followed_by_zero_or_more_bs(" ab"))
