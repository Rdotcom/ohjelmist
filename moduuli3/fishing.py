length = int(input("Anna kuhan pituus: "))

if length < 37:
    print(f"Kuhasta puuttuu {37-length} cm, laske kuha takaisin järveen.")
elif length >= 37:
    print("Kuha on tarpeeksi pitkä!")