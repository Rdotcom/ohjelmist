names = set()

def askname():
    while True:
        name = input("Anna nimi: ")
        if name == "":
            break
        elif name in names:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            names.add(name)
    for name in names:
        print(name)

askname()