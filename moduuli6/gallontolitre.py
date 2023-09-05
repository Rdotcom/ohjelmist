def gallonlitre():
    while True:
        gallons = float(input("Anna gallonat: "))
        if gallons < 0:
            print("Lopetetaan")
            break
        print(gallons * 3.785)

gallonlitre()