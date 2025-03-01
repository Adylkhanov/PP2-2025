import string


alphabet = string.ascii_uppercase

for letter in alphabet:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"Is a {letter}.txt document")
