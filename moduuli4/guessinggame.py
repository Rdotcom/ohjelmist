import random

number = random.randint(1,10)
guess = 0

while guess != number:
    guess = int(input("Arvaa luku väliltä 1-10: "))
    if guess < number:
        print("Luku on suurempi.")
    elif guess > number:
        print("Luku on pienempi.")
    else:
        print("Arvasit oikein!")
        break