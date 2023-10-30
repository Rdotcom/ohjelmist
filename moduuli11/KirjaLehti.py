
class Book:
    def __init__(self,name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.name}\nKirjailija: {self.author}\nSivumäärä: {self.pages}")


class Paper:
    def __init__(self,name, editor):
        self.name = name
        self.editor = editor

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.name}\nPäätoimittaja: {self.editor}")


if __name__ == "__main__":
    lehti = Paper("Aku Ankka", "Aki Hyyppä")
    lehti.tulosta_tiedot()
    kirja = Book("Hytti n:o 6", "Rosa Liksom", 200)
    kirja.tulosta_tiedot()