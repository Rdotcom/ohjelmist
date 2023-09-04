number = int(input("Anna numero: "))

for i in range(2, number):
    if number % i == 0:
        print("Ei ole alkuluku")
        break
    else:
        print("Luku on alkuluku")
        break
        #jako omalla luvullaan?