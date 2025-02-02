from itertools import permutations

def permutation(string):

    p = permutations(string)

    for i in p:
        print("".join(i))


a = input()

permutation(a)