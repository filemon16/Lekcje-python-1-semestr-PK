# Zadanie 1
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        current_value = self.current
        self.current -= 1
        return current_value

countdown = CountDown(5)
for num in countdown:
    print(num)


# Zadanie 2
class ListaLiczbowa:
    def __init__(self, liczby):
        self.liczby = liczby

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.liczby):
            raise StopIteration
        wartosc = self.liczby[self.index]
        self.index += 1
        return wartosc

lista = ListaLiczbowa([10, 20, 30])
for liczba in lista:
    print(liczba)


# Zadanie 3
def countdown_generator(start):
    current = start
    while current > 0:
        yield current
        current -= 1

for num in countdown_generator(5):
    print(num)


# Zadanie 4
def czytaj_linie_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

# for linia in czytaj_linie_pliku('plik.txt'):
#     print(linia)


# Zadanie 5
class ReusableCountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountDownIterator(self.start)

class CountDownIterator:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current_value = self.start
        self.start -= 1
        return current_value

countdown = ReusableCountDown(3)
for i in countdown:
    print(i)
print("Ponownie:")
for i in countdown:
    print(i)


# Zadanie 6
def countdown_single_use(start):
    current = start
    while current > 0:
        yield current
        current -= 1

gen = countdown_single_use(3)
for val in gen:
    print(val)
print("Ponownie (brak danych):")
for val in gen:
    print(val)


# Zadanie 7
from itertools import chain, islice

def polacz_i_wez_pierwsze(*sekwencje, n):
    lancuch = chain(*sekwencje)
    return list(islice(lancuch, n))

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
generator = (x for x in range(7, 10))

wynik = polacz_i_wez_pierwsze(lista1, lista2, generator, n=5)
print(wynik)
