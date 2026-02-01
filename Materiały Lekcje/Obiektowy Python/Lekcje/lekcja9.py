# Zadanie 1
def dodaj(a, b):
    return a + b

def test_dodawania_liczb_dodatnich():
    assert dodaj(2, 3) == 5

def test_dodawania_liczb_ujemnych():
    assert dodaj(-1, -1) == -2


# Zadanie 2
def przetworz_dane(dane):
    if not isinstance(dane, list):
        raise TypeError("Dane muszą być listą")
    return [x * 2 for x in dane if isinstance(x, (int, float))]

def test_przetwarzania_poprawnych_danych():
    assert przetworz_dane([1, 2, 3]) == [2, 4, 6]

def test_przetwarzania_pustej_listy():
    assert przetworz_dane([]) == []

def test_przetwarzania_danych_niepoprawnego_typu():
    try:
        przetworz_dane("nie_lista")
        assert False, "Powinien rzucić TypeError"
    except TypeError:
        pass


# Zadanie 3
def znajdz_najwiekszy_element(lista):
    if not lista:
        return None
    najwiekszy = lista[0]
    for x in lista:
        if x > najwiekszy:
            najwiekszy = x
    return najwiekszy

def test_znalezienia_najwiekszego_elementu():
    assert znajdz_najwiekszy_element([1, 5, 3]) == 5

def test_znalezienia_najwiekszego_dla_pustej_listy():
    assert znajdz_najwiekszy_element([]) is None


# Zadanie 4
from typing import List, Union

def srednia_arytmetyczna(liczby: List[Union[int, float]]) -> float:
    if not liczby:
        return 0.0
    return sum(liczby) / len(liczby)

def test_srednia_arytmetyczna_poprawna():
    assert srednia_arytmetyczna([1, 2, 3]) == 2.0
    assert srednia_arytmetyczna([2.5, 3.5]) == 3.0
    assert srednia_arytmetyczna([]) == 0.0


# Zadanie 5
class KontoBankowe:
    def __init__(self, saldo_poczatkowe: float = 0.0):
        self.saldo = saldo_poczatkowe

    def wplata(self, kwota: float):
        if kwota <= 0:
            raise ValueError("Kwota wpłaty musi być większa od zera")
        self.saldo += kwota

    def wyplata(self, kwota: float):
        if kwota <= 0:
            raise ValueError("Kwota wypłaty musi być większa od zera")
        if kwota > self.saldo:
            raise ValueError("Brak wystarczających środków")
        self.saldo -= kwota

def test_konto_dodatnie_saldo_poczatkowe():
    konto = KontoBankowe(100)
    assert konto.saldo == 100

def test_konto_wplata():
    konto = KontoBankowe(50)
    konto.wplata(25)
    assert konto.saldo == 75

def test_konto_wyplata():
    konto = KontoBankowe(100)
    konto.wyplata(40)
    assert konto.saldo == 60

def test_konto_wyplata_zbyt_duzej_kwoty():
    konto = KontoBankowe(10)
    try:
        konto.wyplata(20)
        assert False, "Powinien rzucić ValueError"
    except ValueError:
        pass
