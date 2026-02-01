# Zadanie 1
# narzedzia.py

import time

def mierz_czas(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        koniec = time.time()
        print(f"Funkcja {funkcja.__name__} wykonała się w {koniec - start:.4f} sekund.")
        return wynik
    return wrapper

# Testowanie modułu
if __name__ == "__main__":
    @mierz_czas
    def przykladowa_funkcja():
        time.sleep(1)
        return "Koniec"

    print(przykladowa_funkcja())

# Zadanie 2
# main.py

import narzedzia

@narzedzia.mierz_czas
def szybka_funkcja():
    return sum(range(100))

@narzedzia.mierz_czas
def wolna_funkcja():
    time.sleep(0.5)
    return "Zrobione!"

szybka_funkcja()
wolna_funkcja()

# Zadanie 3
# Struktura pakietu
# /moj_pakiet
#   |-- __init__.py
#   |-- narzedzia.py
#   |-- raporty.py

# moj_pakiet/__init__.py
"""
Pakiet narzędzi analitycznych v1.0
"""

# moj_pakiet/narzedzia.py
def filtruj_produkty(produkty, minimalna_cena):
    return [p for p in produkty if p['cena'] >= minimalna_cena]

def srednia_cena(produkty):
    if not produkty:
        return 0
    return sum(p['cena'] for p in produkty) / len(produkty)

# moj_pakiet/raporty.py
def raport_top_produktow(produkty, n=3):
    posortowane = sorted(produkty, key=lambda x: x['cena'], reverse=True)
    return posortowane[:n]

# main.py
from moj_pakiet.narzedzia import filtruj_produkty, srednia_cena
from moj_pakiet.raporty import raport_top_produktow

produkty = [
    {'nazwa': 'Laptop', 'cena': 3000},
    {'nazwa': 'Mysz', 'cena': 100},
    {'nazwa': 'Monitor', 'cena': 1200},
    {'nazwa': 'Klawiatura', 'cena': 300},
    {'nazwa': 'Tablet', 'cena': 800}
]

filtr = filtruj_produkty(produkty, 500)
print("Produkty droższe niż 500:", filtr)

srednia = srednia_cena(produkty)
print("Średnia cena:", srednia)

top = raport_top_produktow(produkty, 2)
print("Top 2 produkty:", top)

# Zadanie 4
# pakiet: /analiza_danych
#   |-- __init__.py
#   |-- core/
#       |-- __init__.py
#       |-- przeksztalcenia.py
#       |-- walidacja.py
#   |-- utils/
#       |-- __init__.py
#       |-- pomocnicze.py

# analiza_danych/core/przeksztalcenia.py
def normalizuj_dane(dane):
    if not dane:
        return []
    min_val = min(dane)
    max_val = max(dane)
    if min_val == max_val:
        return [0.0 for _ in dane]
    return [(x - min_val) / (max_val - min_val) for x in dane]

# analiza_danych/core/walidacja.py
def sprawdz_poprawnosc(dane):
    return all(isinstance(x, (int, float)) for x in dane)

# analiza_danych/utils/pomocnicze.py
def sformatuj_wartosci(dane, precyzja=2):
    return [round(x, precyzja) for x in dane]

# analiza_danych/__init__.py
"""
Pakiet do analizy danych w wersji 1.0
"""

# main.py
from analiza_danych.core.przeksztalcenia import normalizuj_dane
from analiza_danych.core.walidacja import sprawdz_poprawnosc
from analiza_danych.utils.pomocnicze import sformatuj_wartosci

dane = [10, 20, 30, 40, 50]
if sprawdz_poprawnosc(dane):
    dane_normal = normalizuj_dane(dane)
    dane_format = sformatuj_wartosci(dane_normal)
    print("Znormalizowane i sformatowane dane:", dane_format)
else:
    print("Dane wejściowe są niepoprawne.")
