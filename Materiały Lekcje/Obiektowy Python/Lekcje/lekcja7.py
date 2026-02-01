# Zadanie 1
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci_generator()
for _ in range(10):
    print(next(gen))


# Zadanie 2
def potegi_dwojki_generator(n):
    potega = 1
    licznik = 0
    while licznik < n:
        yield potega
        potega *= 2
        licznik += 1

for wartosc in potegi_dwojki_generator(5):
    print(wartosc)


# Zadanie 3
import csv

def csv_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

# Przykład użycia (zakładając, że plik 'products.csv' istnieje)
# for product in csv_reader('products.csv'):
#     print(product)


# Zadanie 4
def filtruj_slowa(dlugosc_min, litery_zabronione):
    with open('slowa.txt', 'r', encoding='utf-8') as file:
        for line in file:
            slowo = line.strip()
            if len(slowo) >= dlugosc_min and not any(l in slowo for l in litery_zabronione):
                yield slowo

# Przykład użycia (zakładając, że plik 'slowa.txt' istnieje)
# for slowo in filtruj_slowa(5, ['a', 'b']):
#     print(slowo)


# Zadanie 5
from itertools import groupby

def pogrupuj_linie(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as file:
        for litera, grupa in groupby(file, key=lambda x: x[0].upper()):
            linie = list(grupa)
            yield (litera, linie)

# Przykład użycia (zakładając, że plik 'dane.txt' istnieje)
# for klucz, grupa in pogrupuj_linie('dane.txt'):
#     print(f'Litera {klucz}: {list(grupa)}')


# Zadanie 6
def srednia_ryczałtowa(ryczałty):
    suma = 0
    licznik = 0
    for ryc in ryczałty:
        suma += ryc
        licznik += 1
        if licznik > 0:
            yield suma / licznik

# Przykład użycia
# for srednia in srednia_ryczałtowa([100, 200, 150]):
#     print(srednia)


# Zadanie 7
def chain_custom(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

# Przykład użycia
# for element in chain_custom([1, 2], (3, 4), "AB"):
#     print(element)


# Zadanie 8
def coroutine_generator():
    total = 0
    count = 0
    while True:
        value = yield
        if value is None:
            break
        total += value
        count += 1
        avg = total / count if count > 0 else 0
        yield avg

# Przykład użycia
# coro = coroutine_generator()
# next(coro)  # priming
# print(coro.send(10))  # wysyłamy 10, odbieramy średnią
# next(coro)  # przeskakujemy do kolejnego send
# print(coro.send(20))  # wysyłamy 20, odbieramy nową średnią
# next(coro)
# coro.send(None)  # zakończenie
# coro.close()
