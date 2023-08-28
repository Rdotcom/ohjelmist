cab = input("Anna laivan hyttiluokka (LUX, A, B, C): ").lower()

if cab == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif cab == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif cab == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif cab == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")