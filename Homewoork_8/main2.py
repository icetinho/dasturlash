from os import system
system("cls")

class Texnika:
    brand = "Samsung"
    model = "s24 ultra"
    tip = "telefon"
    narx = 3_000_000

    def __init__(self, brand="artel", model=None, tip=None, narx=None):
        self.brand = brand
        self.model = model
        self.tip = tip
        self.narx = narx
def printINFOS(self):
    print(f"""
brand: = {self.brand}
model: = {self.model}
tip: =   {self.tip}

""")

texnika1 = Texnika("Apple", "iphone 15 pro max", "telefon", "5000000")
texnika2 = Texnika("Samsung", "s24 ultra", "telefon", "3000000")
texnika3 = Texnika("Microfoft", "Surface studio 2", "Monoblok", "5000000"  )
texnika4 = Texnika("Google", "Pixsel 9 pro", "telefon", "3000000")
texnika5 = Texnika("Chevrolet", "Corvet", "Moshina", "10000000")
texnika6 = Texnika("Corsair", "CORSAIR XENEON FLEX", "Monitor", "4000000")
texnika7 = Texnika("Mercedes-Benz", "Brabus g800", "Moshina", "10000000")

sum = 0

TEXNIKALAR = [texnika1, texnika2, texnika3, texnika4, texnika5, texnika6, texnika7]

for texnika in TEXNIKALAR:
    sum += texnika.narx
    print(f"HAMMA SUMMA = {sum} uzs")
