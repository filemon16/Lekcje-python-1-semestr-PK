# Zadanie 1
class Gracz:
    def __init__(self, imie, punkty):
        self.imie = imie
        self.punkty = punkty

    def __eq__(self, other):
        if isinstance(other, Gracz):
            return self.punkty == other.punkty
        return False

    def __lt__(self, other):
        if isinstance(other, Gracz):
            return self.punkty < other.punkty
        return NotImplemented


# Zadanie 2
import random

class Gracz:
    def __init__(self, imie, punkty):
        self.imie = imie
        self.punkty = punkty

    def __eq__(self, other):
        if isinstance(other, Gracz):
            return self.punkty == other.punkty
        return False

    def __lt__(self, other):
        if isinstance(other, Gracz):
            return self.punkty < other.punkty
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Gracz):
            nowe_imie = f"{self.imie}-{other.imie}"
            nowe_punkty = self.punkty + other.punkty
            return Gracz(nowy_imie, nowe_punkty)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Gracz):
            nowe_punkty = abs(self.punkty - other.punkty)
            return Gracz(self.imie, nowe_punkty)
        return NotImplemented

    def __mul__(self, liczba):
        if isinstance(liczba, (int, float)):
            nowe_punkty = self.punkty * liczba
            return Gracz(self.imie, nowe_punkty)
        return NotImplemented

    def __truediv__(self, liczba):
        if isinstance(liczba, (int, float)) and liczba != 0:
            nowe_punkty = self.punkty / liczba
            return Gracz(self.imie, int(nowe_punkty))
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, Gracz):
            nowe_punkty = self.punkty % other.punkty
            return Gracz(self.imie, nowe_punkty)
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, Gracz):
            nowe_punkty = self.punkty ** other.punkty
            return Gracz(self.imie, nowe_punkty)
        return NotImplemented

    def __str__(self):
        return f"Gracz {self.imie} ma {self.punkty} punktów."

    def __repr__(self):
        return f"Gracz(imie='{self.imie}', punkty={self.punkty})"


# Demonstracja
gracz1 = Gracz("Jan", 10)
gracz2 = Gracz("Anna", 5)

print(gracz1 + gracz2)
print(gracz1 - gracz2)
print(gracz1 * 2)
print(gracz1 / 2)
print(gracz1 % gracz2)
print(gracz1 ** gracz2)
print(repr(gracz1))


# Zadanie 3
from functools import total_ordering

@total_ordering
class Gracz:
    def __init__(self, imie, punkty):
        self.imie = imie
        self.punkty = punkty

    def __eq__(self, other):
        if isinstance(other, Gracz):
            return self.punkty == other.punkty
        return False

    def __lt__(self, other):
        if isinstance(other, Gracz):
            return self.punkty < other.punkty
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Gracz):
            nowe_imie = f"{self.imie}-{other.imie}"
            nowe_punkty = self.punkty + other.punkty
            return Gracz(nowy_imie, nowe_punkty)
        return NotImplemented

    def __str__(self):
        return f"Gracz {self.imie} ma {self.punkty} punktów."


# Demonstracja
gracz1 = Gracz("Jan", 10)
gracz2 = Gracz("Anna", 5)

print(gracz1 >= gracz2)
print(gracz1 <= gracz2)


# Zadanie 4
class Ekwipunek:
    def __init__(self):
        self._przedmioty = []

    def __len__(self):
        return len(self._przedmioty)

    def __getitem__(self, index):
        return self._przedmioty[index]

    def __setitem__(self, index, value):
        if index < len(self._przedmioty):
            self._przedmioty[index] = value
        else:
            raise IndexError("Indeks poza zakresem")

    def __delitem__(self, index):
        if index < len(self._przedmioty):
            del self._przedmioty[index]
        else:
            raise IndexError("Indeks poza zakresem")

    def append(self, item):
        self._przedmioty.append(item)

    def __iter__(self):
        return iter(self._przedmioty)

    def __repr__(self):
        return f"Ekwipunek({self._przedmioty})"


# Demonstracja
ekwipunek = Ekwipunek()
ekwipunek.append("Miecz")
ekwipunek.append("Tarcza")
ekwipunek.append("Hełm")

print(len(ekwipunek))
print(ekwipunek[0])
ekwipunek[1] = "Zbroja"
print(ekwipunek)
del ekwipunek[2]
print(ekwipunek)

for przedmiot in ekwipunek:
    print(przedmiot)
