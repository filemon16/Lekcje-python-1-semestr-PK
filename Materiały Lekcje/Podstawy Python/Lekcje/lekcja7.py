# Zadanie 1
def przygotuj_pizze(dodatki, baza=None):
    if baza is None:
        baza = ["sos", "ser"]
    return baza + dodatki

pierwsza_pizza = przygotuj_pizze(["pieczarki"])
druga_pizza = przygotuj_pizze(["szynka", "cebula"])

print("Pierwsza pizza:", pierwsza_pizza)
print("Druga pizza:", druga_pizza)

# Zadanie 2
kontakty = {"Anna": "123", "Piotr": "456"}
print(f"Początkowe kontakty: {kontakty}")

nazwy_kontaktow = kontakty.keys()
print(f"Pobrane nazwy: {nazwy_kontaktow}")

print("\nDodajemy nowy kontakt 'Zofia'...")
kontakty["Zofia"] = "789"

print(f"Aktualne kontakty: {kontakty}")
print(f"Nazwy kontaktów po zmianie: {nazwy_kontaktow}")

# Zadanie 3
def poprawny_styl(nazwa_pliku):
    if not nazwa_pliku.endswith('.py'):
        nazwa_pliku += '.py'
    return nazwa_pliku.replace(' ', '_').lower()

print(poprawny_styl("To jest przykładowy napis"))
print(poprawny_styl("Nasiona.py"))

# Zadanie 4
def sformatuj_dane(osoba):
    imie = osoba.get("imie", "").strip().capitalize()
    nazwisko = osoba.get("nazwisko", "").strip().upper()
    wiek = osoba.get("wiek", 0)
    return {
        "imie": imie,
        "nazwisko": nazwisko,
        "wiek": wiek
    }

dane = {"imie": " anna ", "nazwisko": " kowalska ", "wiek": 25}
print(sformatuj_dane(dane))

# Zadanie 5
def oblicz_dane(data):
    suma = 0
    licznik = 0
    for item in data:
        if isinstance(item, (int, float)):
            suma += item
            licznik += 1
    srednia = suma / licznik if licznik > 0 else 0
    return {"suma": suma, "srednia": srednia}

print(oblicz_dane([1, 2, 3, 4]))
print(oblicz_dane([]))
