import random

dices = int(input("Anna arpakuutioiden lukumäärä: "))
sum = 0

for i in range(dices):
    dice = random.randint(1,6)
    sum+=dice
print(f"Arpakuutioiden lukujen summa on {sum}")