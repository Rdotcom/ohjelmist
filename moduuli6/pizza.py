import math

def laskepizza(halkaisija, hinta):
    pintaala = ((math.pi / 4) * halkaisija ** 2)
    yhteishinta = hinta / pintaala
    return yhteishinta

def pizzat():
    halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
    hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))
    halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
    hinta2 = float(input("Anna toisen pizzan hinta: "))

    yhteishinta1 = laskepizza(halkaisija1, hinta1)
    yhteishinta2 = laskepizza(halkaisija2, hinta2)

    if yhteishinta2 < yhteishinta1:
        print(f"Toinen pizza saa paremman hinnan {yhteishinta2:.2f}€ per neliömetri")
    elif yhteishinta1 < yhteishinta2:
        print(f"Ensimmäinen pizza saa paremman hinnan {yhteishinta1:.2f}€ per neliömetri")
    else:
        print(f"Molemmat pizzat ovat yhtä kalliita")


pizzat()
