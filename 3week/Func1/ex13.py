from wsgiref.util import guess_scheme
import random

def guess_num():
    print("Hello! What is your name?")
    name = input()

    print ( f"Well, {name}, I am thinking of a number between 1 and 20.")

    print("Take a guess.")

    c = int(input())

    steps = 1

    num = random.randint(1,20)

    while(True):
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


guess_num()