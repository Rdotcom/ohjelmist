user = "python"
password = "rules"
tries = 0

while True:
    tries += 1
    userinput = input("Anna käyttäjätunnus: ")
    passinput = input("Anna salasana: ")
    if userinput == user and passinput == password:
        print("Tervetuloa")
        break
    elif tries == 5:
        print("Pääsy evätty")
        break
    else:
        print("Virheellinen käyttäjätunnus tai salasana.")

