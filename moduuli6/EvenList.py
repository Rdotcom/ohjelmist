def parilliset(lista:list):
    parillisetlista = []
    for i in lista:
        if i % 2 == 0:
            parillisetlista.append(i)
    return parillisetlista

def main():
    lista = [1,5,3,2,14,9,20]
    print(lista)
    print("-----------------------")
    print(parilliset(lista))

main()
