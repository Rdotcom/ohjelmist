airports = {}

def main():
    while True:
        print("1) Uusi lentokenttä")
        print("2) Etsi lentokenttiä")
        print("3) Lopeta")
        valinta = int(input("Valintasi: "))

        if valinta == 1:
            icao = input("Anna lentokentän ICAO-koodi: ")
            name = input("Anna lentokentän nimi: ")
            airports[icao] = name

        elif valinta == 2:
            icao = input("Anna lentokentän ICAO-koodi: ")
            if icao in airports:
                print("Lentoasema:",airports[icao])
            else:
                print("Lentokenttää ei löydy")

        elif valinta == 3:
            break
        else:
            print("Virheellinen valinta!")

main()
