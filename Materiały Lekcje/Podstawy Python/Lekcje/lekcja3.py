# Zadanie 1
zakupy = []
while True:
    produkt = input("Podaj produkt (lub 'koniec'): ")
    if produkt == "koniec":
        break
    zakupy.append(produkt)
print("Twoja lista zakupów:")
for i, prod in enumerate(zakupy, 1):
    print(f"{i}. {prod}")

# Zadanie 2
punkt_startowy = (0, 0)
print(punkt_startowy)
# punkt_startowy[0] = 10  # To spowoduje błąd

# Zadanie 3
numery_lotto = [5, 12, 5, 42, 12, 9]
zbior_unikalny = set(numery_lotto)
lista_posortowana = sorted(list(zbior_unikalny))
print(lista_posortowana)

# Zadanie 4
tagi_wejscie = input("Podaj tagi oddzielone przecinkami: ")
lista_tagow = tagi_wejscie.split(",")
oczyszczona_lista = [tag.strip() for tag in lista_tagow]
unikalne_tagi = set(oczyszczona_lista)
print(f"Liczba wszystkich podanych tagów: {len(oczyszczona_lista)}")
print(f"Liczba unikalnych tagów: {len(unikalne_tagi)}")
print("Unikalne tagi (alfabetycznie):")
for tag in sorted(unikalne_tagi):
    print(f"- {tag}")

# Zadanie 5
znajomi_anny = ["Piotr", "Zofia", "Marek", "Anna"]
znajomi_piotra = ["Anna", "Marek", "Krzysztof", "Ewa"]
set_anna = set(znajomi_anny)
set_piotr = set(znajomi_piotra)
wspolni = set_anna & set_piotr
print(wspolni)

# Zadanie 6
wizytowka = {
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "stanowisko": "Programista"
}
print(f"{wizytowka['imie']} {wizytowka['nazwisko']}")
print(wizytowka["stanowisko"])

# Zadanie 7
kontakty = {}
while True:
    print("1. Dodaj kontakt")
    print("2. Wyświetl kontakt")
    print("3. Usuń kontakt")
    print("4. Wyświetl wszystko")
    print("5. Zakończ")
    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        nazwa = input("Podaj nazwę kontaktu: ")
        numer = input("Podaj numer telefonu: ")
        kontakty[nazwa] = numer
        print("Kontakt dodany.")
    elif wybor == "2":
        nazwa = input("Podaj nazwę kontaktu: ")
        if nazwa in kontakty:
            print(f"Numer: {kontakty[nazwa]}")
        else:
            print("Kontakt nie znaleziony.")
    elif wybor == "3":
        nazwa = input("Podaj nazwę kontaktu do usunięcia: ")
        if nazwa in kontakty:
            del kontakty[nazwa]
            print("Kontakt usunięty.")
        else:
            print("Kontakt nie znaleziony.")
    elif wybor == "4":
        if not kontakty:
            print("--- BRAK KONTAKTÓW ---")
        else:
            print("--- MOJE KONTAKTY ---")
            for nazwa, numer in kontakty.items():
                print(f"Nazwa: {nazwa}, Numer: {numer}")
            print("--- KONIEC LISTY ---")
    elif wybor == "5":
        break

# Zadanie 8
baza_danych = [
    {"imie": "Anna", "stanowisko": "Specjalista", "pensja": 4500},
    {"imie": "Piotr", "stanowisko": "Manager", "pensja": 8000},
    {"imie": "Zofia", "stanowisko": "Specjalista", "pensja": 5200},
    {"imie": "Krzysztof", "stanowisko": "Stażysta", "pensja": 2500}
]

suma_pensji = 0
for pracownik in baza_danych:
    suma_pensji += pracownik["pensja"]
srednia_pensja = suma_pensji / len(baza_danych)
print(f"Średnia pensja: {srednia_pensja}")

najwyzsza_pensja = 0
pracownik_max = None
for pracownik in baza_danych:
    if pracownik["pensja"] > najwyzsza_pensja:
        najwyzsza_pensja = pracownik["pensja"]
        pracownik_max = pracownik
print(f"Najwyższa pensja: {pracownik_max}")

print("Imiona specjalistów:")
for pracownik in baza_danych:
    if pracownik["stanowisko"] == "Specjalista":
        print(pracownik["imie"])
