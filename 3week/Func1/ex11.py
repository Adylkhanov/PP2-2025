def palindrome(word):

    word = word.lower()
    s = "".join(word.split())

    print(s)
    print(s[::-1])

    return s == s[::-1]

print(palindrome("tenet"))
print(palindrome("аргентина манит негра"))