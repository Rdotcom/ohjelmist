import random

lock3 = []
lock4 = []

while len(lock3)<3:
    lock3.append(random.randint(0,9))
print(lock3)

while len(lock4)<4:
    lock4.append(random.randint(1,6))
print(lock4)
