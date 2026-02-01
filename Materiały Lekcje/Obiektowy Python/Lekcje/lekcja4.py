# Zadanie 1
with open("dziennik.txt", "w") as plik:
    plik.write("Pierwszy wpis do dziennika.\n")

with open("dziennik.txt", "r") as plik:
    zawartosc = plik.read()
    print("Zawartość po zapisie:")
    print(zawartosc)

with open("dziennik.txt", "a") as plik:
    plik.write("Drugi wpis do dziennika.\n")

with open("dziennik.txt", "a") as plik:
    plik.write("Trzeci wpis do dziennika.\n")

with open("dziennik.txt", "r") as plik:
    zawartosc = plik.read()
    print("Zawartość po dodaniu trzech linii:")
    print(zawartosc)


# Zadanie 2
try:
    with open("brak.txt", "r") as plik:
        print(plik.read())
except FileNotFoundError:
    print("Plik nie istnieje.")

try:
    liczba = int("abc")
except ValueError:
    print("Niepoprawny format liczby.")


# Zadanie 3
# Już zaimplementowane w Zadaniu 1 za pomocą `with`.


# Zadanie 4
class ZlyLogin(Exception):
    pass


def sprawdz_login(login):
    if len(login) < 3:
        raise ZlyLogin("Login musi mieć co najmniej 3 znaki.")


try:
    sprawdz_login("ab")
except ZlyLogin as e:
    print(e)


# Zadanie 5
class MenedzerPliku:
    def __init__(self, sciezka, tryb):
        self.sciezka = sciezka
        self.tryb = tryb
        self.plik = None

    def __enter__(self):
        self.plik = open(self.sciezka, self.tryb)
        return self.plik

    def __exit__(self, exc_type, exc_value, traceback):
        if self.plik:
            self.plik.close()


with MenedzerPliku("test_menadzera.txt", "w") as plik:
    plik.write("Test własnego menedżera kontekstu.")


# Zadanie 6
import os
import tempfile

def bezpieczny_zapis(sciezka, dane):
    _, temp_sciezka = tempfile.mkstemp(dir=os.path.dirname(sciezka))
    with open(temp_sciezka, "w") as temp_plik:
        temp_plik.write(dane)
    os.replace(temp_sciezka, sciezka)


bezpieczny_zapis("config.json", '{"klucz": "wartosc"}')


# Zadanie 7
def zlicz_bledy(sciezka_pliku):
    liczba_bledow = 0
    try:
        with open(sciezka_pliku, "r") as plik:
            for linia in plik:
                try:
                    poziom, _ = linia.split(":", 1)
                    if poziom.strip().upper() == "ERROR":
                        liczba_bledow += 1
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"Plik {sciezka_pliku} nie istnieje.")
    return liczba_bledow


# Zadanie 8
class TlumikWyjatkow:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return True


with TlumikWyjatkow():
    x = 1 / 0

print("Wyjątek został stłumiony.")
