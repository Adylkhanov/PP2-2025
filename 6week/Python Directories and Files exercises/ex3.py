import os

def testa(path):
    if os.access(path, os.F_OK):
        print("Exist")
        print(f"Filename:{os.path.basename(path)}")
        print(f"Dir:{os.path.dirname(path)}")
    else:
        print("dont exist")

testa(str(input()))
