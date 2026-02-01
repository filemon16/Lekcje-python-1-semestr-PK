# Zadanie 1
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def przedstaw_sie(self):
        print(f"Gracz {self.imie} ma {self.hp} punktów życia.")


# Kod "Przed" (proceduralny)
gracz_slownik = {"imie": "Marek", "hp": 100}


def przedstaw_gracza(gracz):
    print(f"Gracz {gracz['imie']} ma {gracz['hp']} punktów życia.")


# Demonstracja
print("Kod proceduralny:")
przedstaw_gracza(gracz_slownik)

print("\nKod obiektowy:")
gracz_obiekt = Gracz("Marek", 100)
gracz_obiekt.przedstaw_sie()


# Zadanie 2
class Postac:
    def __init__(self, imie, hp, sila, inteligencja):
        self.imie = imie
        self.hp = hp
        self.sila = sila
        self.inteligencja = inteligencja

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}. Moje HP: {self.hp}")


class Wojownik(Postac):
    def __init__(self, imie, hp, sila, inteligencja):
        super().__init__(imie, hp, sila, inteligencja)
        self.profesja = "Wojownik"

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}, {self.profesja} o sile {self.sila}.")


class Mag(Postac):
    def __init__(self, imie, hp, sila, inteligencja):
        super().__init__(imie, hp, sila, inteligencja)
        self.profesja = "Mag"

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}, {self.profesja} o inteligencji {self.inteligencja}.")


# Demonstracja
print("\nDemonstracja klas potomnych:")
wojownik = Wojownik("Geralt", 100, 20, 10)
mag = Mag("Yennefer", 80, 5, 25)

wojownik.przedstaw_sie()
mag.przedstaw_sie()


# Zadanie 3
class Postac:
    def __init__(self, imie, hp, sila, inteligencja):
        self._imie = imie
        self._hp = hp
        self._sila = sila
        self._inteligencja = inteligencja

    @property
    def imie(self):
        return self._imie

    @property
    def hp(self):
        return self._hp

    @property
    def sila(self):
        return self._sila

    @property
    def inteligencja(self):
        return self._inteligencja

    def przedstaw_sie(self):
        print(f"Jestem {self._imie}. Moje HP: {self._hp}")


class Wojownik(Postac):
    def __init__(self, imie, hp, sila, inteligencja):
        super().__init__(imie, hp, sila, inteligencja)
        self.profesja = "Wojownik"

    def przedstaw_sie(self):
        print(f"Jestem {self._imie}, {self.profesja} o sile {self._sila}.")


class Mag(Postac):
    def __init__(self, imie, hp, sila, inteligencja):
        super().__init__(imie, hp, sila, inteligencja)
        self.profesja = "Mag"

    def przedstaw_sie(self):
        print(f"Jestem {self._imie}, {self.profesja} o inteligencji {self._inteligencja}.")


# Demonstracja
print("\nDemonstracja enkapsulacji (@property):")
wojownik = Wojownik("Ciri", 90, 18, 12)
print(f"Dostęp do imienia: {wojownik.imie}")
print(f"Dostęp do HP: {wojownik.hp}")
wojownik.przedstaw_sie()


# Zadanie 4
class Postac:
    def __init__(self, imie, hp, sila, inteligencja):
        self._imie = imie
        self._hp = hp
        self._sila = sila
        self._inteligencja = inteligencja

    @property
    def imie(self):
        return self._imie

    @property
    def hp(self):
        return self._hp

    @property
    def sila(self):
        return self._sila

    @property
    def inteligencja(self):
        return self._inteligencja

    def przedstaw_sie(self):
        print(f"Jestem {self._imie}. Moje HP: {self._hp}")


class Wojownik(Postac):
    def __init__(self, imie, hp, sila, inteligencja):
        super().__init__(imie, hp, sila, inteligencja)
        self.profesja = "Wojownik"

    def przedstaw_sie(self):
        print(f"Jestem {self._imie}, {self.profesja} o sile {self._sila}.")


class Mag(Postac):
    def __init__(self, imie, hp, sila, inteligencja):
        super().__init__(imie, hp, sila, inteligencja)
        self.profesja = "Mag"

    def przedstaw_sie(self):
        print(f"Jestem {self._imie}, {self.profesja} o inteligencji {self._inteligencja}.")


class Bestia(Postac):
    def __init__(self, imie, hp, sila, inteligencja):
        super().__init__(imie, hp, sila, inteligencja)
        self.profesja = "Bestia"

    def przedstaw_sie(self):
        print(f"Rrrrr... Jestem {self._imie}, {self.profesja}. Moje HP: {self._hp}.")


# Demonstracja
print("\nDemonstracja polimorfizmu:")
druzyna = [Wojownik("Conan", 120, 25, 8), Mag("Gandalf", 100, 5, 30), Bestia("Fenrir", 150, 30, 2)]

for postac in druzyna:
    postac.przedstaw_sie()
