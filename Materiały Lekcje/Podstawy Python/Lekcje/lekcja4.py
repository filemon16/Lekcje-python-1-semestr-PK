# Zadanie 1
def wyswietl_powitanie():
    print("+++++++++++++++++++++++++++++++")
    print("         Witaj, Użytkowniku!         ")
    print("+++++++++++++++++++++++++++++++")


wyswietl_powitanie()
wyswietl_powitanie()


# Zadanie 2
def przedstaw_sie(nazwa_uzytkownika):
    print(f"Cześć, jestem {nazwa_uzytkownika}. Miło mi Cię poznać.")


imie = input("Jak masz na imię? ")
przedstaw_sie(imie)


# Zadanie 3
def dodaj(liczba1, liczba2):
    suma = liczba1 + liczba2
    return suma


wynik_dodawania = dodaj(5, 7)
print(wynik_dodawania)


# Zadanie 4
def generuj_raport(imie, stanowisko="Pracownik", miasto="Nieznane"):
    print(f"Imię: {imie}")
    print(f"Stanowisko: {stanowisko}")
    print(f"Miasto: {miasto}")


generuj_raport("Adam")
print()
generuj_raport("Barbara", miasto="Warszawa")
print()
generuj_raport(miasto="Kraków", imie="Celina", stanowisko="Kierownik")


# Zadanie 5
import math

def oblicz_pole(figura, a=0, b=0, r=0):
    """
    Oblicza pole prostokąta lub koła.

    Args:
        figura: Typ figury ("prostokat" lub "kolo").
        a: Długość boku a (dla prostokąta) lub promień (dla koła).
        b: Długość boku b (dla prostokąta).

    Returns:
        Pole figury lub None, jeśli figura jest nieznana.
    """
    if figura == "prostokat":
        return a * b
    elif figura == "kolo":
        return math.pi * r ** 2
    else:
        return None


print(oblicz_pole("prostokat", a=5, b=3))
print(oblicz_pole("kolo", r=2))
help(oblicz_pole)


# Zadanie 6
def rozdziel_imie_nazwisko(imie_i_nazwisko):
    lista_im_nazw = imie_i_nazwisko.split()
    imie = lista_im_nazw[0]
    nazwisko = lista_im_nazw[1]
    return imie, nazwisko


im, naz = rozdziel_imie_nazwisko("Jan Kowalski")
print(f"Imię: {im}")
print(f"Nazwisko: {naz}")


# Zadanie 7
def zsumuj_wszystko(*liczby):
    return sum(liczby)


print(zsumuj_wszystko(1, 2, 3))
print(zsumuj_wszystko(10, 20, 30, 40, 50))


# Zadanie 8
def generuj_raport(**szczegoly):
    for klucz, wartosc in szczegoly.items():
        print(f"{klucz}: {wartosc}")


generuj_raport(status="Aktywny", punkty=150)
print()
generuj_raport(imie="Anna", kraj="Polska", wiek=30)


# Zadanie 9
def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def wykonaj_operacje(a, b, funkcja_operacji):
    return funkcja_operacji(a, b)


wynik_dodawania = wykonaj_operacje(10, 5, dodaj)
wynik_odejmowania = wykonaj_operacje(10, 5, odejmij)

print(f"Wynik dodawania: {wynik_dodawania}")
print(f"Wynik odejmowania: {wynik_odejmowania}")
