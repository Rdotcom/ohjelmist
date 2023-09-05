import random

def throw_dice():
    while True:
        dice = random.randint(1,6)
        print(f"Arpakuution luku on {dice}")
        if dice == 6:
            return "Sait kuutosen!"

print(throw_dice())
