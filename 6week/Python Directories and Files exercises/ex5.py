from importlib.metadata import files


def funcex5(fname, lname):
    file = open(fname , "w")
    for x in lname:
        file.writelines(f"{x}\n")
    file.close()

a = ["Alisher" , "Adylkhanov", "Aidarkhanovich", "is", "a", "student"]
name = str(input())

funcex5(name, a)
