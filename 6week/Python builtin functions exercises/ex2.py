from curses.ascii import isupper, islower


def upandlowe(st):
    upp = sum(1 for x in st if isupper(x))
    low = sum(1 for x in st if islower(x))

    print( f"low :{low}, upp = {upp}")


s = input()

upandlowe(s)
