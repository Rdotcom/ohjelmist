import random

def dices():
    dicenumber = int(input("Anna arpakuution maksimisilmäluku: "))
    while True:
        dice = random.randint(1,dicenumber)
        print(f"Arpakuution luku on {dice}")
        if dice == dicenumber:
            return f"Sait {dicenumber}!"

print(dices())
