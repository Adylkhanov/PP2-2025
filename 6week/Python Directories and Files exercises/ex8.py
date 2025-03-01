import os

def deletefiles(path):

    if not os.path.exists(path):
        print("Sorry, path dont exist")

        return
    elif not os.access(path, os.W_OK):
        print("Sorry, you dont have access")
        return
    else:
        os.remove(path)
        print("its deleted")
        return

deletefiles(str(input()))
