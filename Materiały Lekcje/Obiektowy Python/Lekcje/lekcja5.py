# Zadanie 1
import os

sciezka = os.path.join("dane", "uzytkownicy", "jan_kowalski.txt")
print(sciezka)


# Zadanie 2
class Gracz:
    def __init__(self, imie, punkty):
        self.imie = imie
        self.punkty = punkty

    def __repr__(self):
        return f"Gracz(imie='{self.imie}', punkty={self.punkty})"

    def __getstate__(self):
        return {"imie": self.imie, "punkty": self.punkty}

    def __setstate__(self, state):
        self.imie = state["imie"]
        self.punkty = state["punkty"]


# Zadanie 3
import csv

def wczytaj_produkty_csv(sciezka):
    produkty = []
    try:
        with open(sciezka, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    row['cena'] = float(row['cena'])
                    row['ilosc'] = int(row['ilosc'])
                except ValueError:
                    continue
                produkty.append(row)
    except FileNotFoundError:
        print(f"Plik {sciezka} nie istnieje.")
    return produkty


# Zadanie 4
import csv

def zapisz_produkty_csv(sciezka, lista_produktow):
    if not lista_produktow:
        return

    with open(sciezka, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['nazwa', 'cena', 'ilosc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for produkt in lista_produktow:
            writer.writerow(produkt)


# Zadanie 5
import json

def wczytaj_konfiguracje(sciezka):
    try:
        with open(sciezka, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Plik {sciezka} nie istnieje.")
        return {}


# Zadanie 6
import json

def zapisz_konfiguracje(sciezka, dane):
    with open(sciezka, 'w', encoding='utf-8') as f:
        json.dump(dane, f, indent=4, ensure_ascii=False)


# Zadanie 7
def przetworz_raport(plik):
    zawartosc = plik.read()
    print(zawartosc)


# Zadanie 8
import io
import csv

def generuj_csv_w_pamieci(dane):
    output = io.StringIO()
    writer = csv.writer(output)
    for wiersz in dane:
        writer.writerow(wiersz)
    return output.getvalue()

dane_testowe = [["Imie", "Nazwisko"], ["Jan", "Kowalski"], ["Anna", "Nowak"]]
csv_jako_string = generuj_csv_w_pamieci(dane_testowe)
print(csv_jako_string)
