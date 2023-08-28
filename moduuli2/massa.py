import math

lei = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))
massa = (8512*lei+425.6*naula+13.3*luoti)


print(f"Massa nykymittojen mukaan:\n{int(massa)//1000} kilogrammaa ja {massa%1000:.2f} grammaa")


