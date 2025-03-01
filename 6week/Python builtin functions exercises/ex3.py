
def ispalindrome(s):
    if s == s[::-1]:
        print("Test is passed")
    else:
        print("Test is not passed")

s = input()
s.lower()
ispalindrome(s)


