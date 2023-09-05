def sumlist(lista:list):
    summalista = []
    for i in lista:
        summalista.append(i)
    return sum(summalista)

def main():
    lista = [1,2,3,4,5,9]
    print(sumlist(lista))

main()