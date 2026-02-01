# Zadanie 1
wiek = int(input("Podaj swój wiek: "))
if wiek >= 18:
    print("Jesteś pełnoletni!")
print("Dziękujemy za skorzystanie z usługi.")

# Zadanie 2
wiek = int(input("Podaj swój wiek: "))
if wiek < 13:
    print("Jesteś dzieckiem.")
elif wiek <= 17:
    print("Jesteś nastolatkiem.")
elif wiek <= 64:
    print("Jesteś dorosłym.")
else:
    print("Jesteś seniorem.")

# Zadanie 3
punkty = int(input("Podaj liczbę punktów z kolokwium (0-100): "))
if punkty <= 50:
    print("Ocena: 2.0")
elif punkty <= 60:
    print("Ocena: 3.0")
elif punkty <= 70:
    print("Ocena: 3.5")
elif punkty <= 80:
    print("Ocena: 4.0")
elif punkty <= 90:
    print("Ocena: 4.5")
else:
    print("Ocena: 5.0")

# Zadanie 4
wiek = int(input("Podaj swój wiek: "))
wzrost = int(input("Podaj swój wzrost w cm: "))
zgoda_opiekuna = input("Czy masz zgodę opiekuna? (tak/nie): ")

if wzrost >= 140 and (wiek >= 18 or zgoda_opiekuna == "tak"):
    print("Możesz wejść!")
else:
    print("Niestety, nie spełniasz warunków.")

# Zadanie 5
licznik = 5
while licznik > 0:
    print(licznik)
    licznik -= 1
print("Start!")

# Zadanie 6
while True:
    slowo = input("Napisz coś (wpisz 'koniec' aby zakończyć): ")
    if slowo == "koniec":
        break
    print(slowo)

# Zadanie 7
while True:
    komenda = input("Wprowadź komendę: ")
    if komenda == "koniec":
        break
    if komenda.startswith("#"):
        continue
    print(f"Wykonuję: {komenda}")

# Zadanie 8
slowo = input("Podaj słowo: ").lower()
SAMOGLOSKI = "aeiouy"
licznik_samoglosek = 0

for litera in slowo:
    if litera in SAMOGLOSKI:
        licznik_samoglosek += 1

print(f"Liczba samogłosek w słowie '{slowo}' to: {licznik_samoglosek}")

# Zadanie 9
for i in range(5):
    print(f"To jest powtórzenie numer: {i + 1}")

# Zadanie 10
for liczba in range(1, 101):
    if liczba % 3 == 0 and liczba % 5 == 0:
        print("FizzBuzz")
    elif liczba % 3 == 0:
        print("Fizz")
    elif liczba % 5 == 0:
        print("Buzz")
    else:
        print(liczba)
