from itertools import permutations
from wsgiref.util import guess_scheme

def transfer(grams):
    ounces = 28.3495231 * grams
    return ounces

def temp(f):
    c = (5 / 9) * (f - 32)
    return c

def solve(numheads, legs):

    chickens = numheads*2
    rabs = int((legs - chickens)/2)

    print(f"rabs: {rabs}, chickens: {numheads}")



def filter_prime(numbers):
    lict =[]

    for num in  numbers:
        primefactor = True
        for i in range(2, num):
            if num % i == 0:
                primefactor = False
                break
        if primefactor and num != 1:
            lict.append(num)




    return lict

def permutation(string):

    p = permutations(string)

    for i in p:
        print("".join(i))

def reverse(string):
    return " ".join(string.split()[::-1])

def has_33(lict):

    for i in range(len(lict) - 1):
        if lict[i] == 3 and lict[i+1] == 3:
            return True
    return False

def spy_game(lict):
    spy_number =[0,0,7]

    for i in lict:
        if i == spy_number[0]:
            spy_number.pop(0)
        if  not spy_number:
            return True
    return False

def volume(rad):
    return ((4*3.14*(rad**3))/3)

def set2(lict):
    container = []
    for i in lict:
          if i not in container:
              container.append(i)


    return  container

def palindrome(word):

    word = word.lower()
    s = "".join(word.split())

    print(s)
    print(s[::-1])

    return s == s[::-1]

def histogram(lict):
    for i in lict:
        print(i*'*')


import random

def guess_num():
    print("Hello! What is your name?")
    name = input()

    print ( f"Well, {name}, I am thinking of a number between 1 and 20.")

    print("Take a guess.")

    c = int(input())

    steps = 1

    num = random.randint(1,20)

    while True:
        print()
        if c > num:

            print("Your guess is too high")

        elif c < num:

            print("Your guess is too low")

        else:
            print(f"Good job, {name}! You guessed my number in {steps} guesses!")
            break
        print("Take a guess.")
        c = int(input())
        steps +=1




