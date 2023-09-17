vuodenajat = {
    1: "kevät", 2: "kevät", 3: "kevät",
    4: "kesä", 5: "kesä", 6: "kesä",
    7: "syksy", 8: "syksy", 9: "syksy",
    10: "talvi", 11: "talvi", 12: "talvi"
}
def time_of_year():
    kuukaus = int(input("Anna kuukausi numerona: "))
    if kuukaus < 1 or kuukaus > 12:
        print("Virheellinen syöte!")
    else:
        print(vuodenajat[kuukaus])

time_of_year()