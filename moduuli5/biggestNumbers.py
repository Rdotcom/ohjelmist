numbers = []

while True:
    number = input("Anna numero: ")
    if number == "":
        break
    numbers.append(int(number))

numbers.sort(reverse=True)
print(f"Suurimmat numerot:", numbers[0:5])