


def copypast(fisrtf, secondf):
    f1 = open(fisrtf, "r")
    f2 = open(secondf, "w")

    a = f1.read()

    for x in a:
        f2.writelines(x)


original = str(input("Original: "))
fake = str(input("Fake: "))

copypast(original, fake)

