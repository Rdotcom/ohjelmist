gender = input("Anna sukupuolesi: ").lower()
value = int(input("Anna hemoglobiiniarvo (g/l): "))

if gender == "mies" and value >195:
    print("Hemoglobiiniarvo on korkea")
elif gender == "mies" and 134<=value<=195:
    print("Hemoglobiiniarvo on normaali")
elif gender == "mies" and value<134:
    print("Hemoglobiiniarvo on alhainen")

if gender == "nainen" and value>175:
    print("Hemoglobiiniarvo on korkea")
elif gender == "nainen" and 117<=value<=175:
    print("Hemoglobiiniarvo on normaali")
elif gender == "nainen" and value<117:
    print("Hemoglobiiniarvo on alhainen")
