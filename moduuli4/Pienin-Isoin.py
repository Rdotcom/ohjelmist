luku = 1
luvut = []

while luku != "":
    luku = (input("Anna luku: "))
    if luku != "":
        luvut.append(int(luku))

print("Pienin luku on", min(luvut))
print("Suurin luku on", max(luvut))