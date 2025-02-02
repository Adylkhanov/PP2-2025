def reverse(string):
    return " ".join(string.split()[::-1])


a = input()

print(reverse(a))