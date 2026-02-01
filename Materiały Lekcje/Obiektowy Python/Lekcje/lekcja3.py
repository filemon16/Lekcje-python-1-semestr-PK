# Zadanie 1
class Gracz:
    def __init__(self, imie, hp, sila, inteligencja):
        self._imie = imie
        self._hp = hp
        self._sila = sila
        self._inteligencja = inteligencja

    def __repr__(self):
        return f"Gracz(imie='{self._imie}', hp={self._hp}, sila={self._sila}, inteligencja={self._inteligencja})"

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila, inteligencja):
        super().__init__(imie, hp, sila, inteligencja)

    def __repr__(self):
        return f"Wojownik(imie='{self._imie}', hp={self._hp}, sila={self._sila}, inteligencja={self._inteligencja})"

class Mag(Gracz):
    def __init__(self, imie, hp, sila, inteligencja):
        super().__init__(imie, hp, sila, inteligencja)

    def __repr__(self):
        return f"Mag(imie='{self._imie}', hp={self._hp}, sila={self._sila}, inteligencja={self._inteligencja})"

def fabryka_postaci(typ: str, imie: str):
    if typ.lower() == "wojownik":
        return Wojownik(imie, hp=120, sila=20, inteligencja=5)
    elif typ.lower() == "mag":
        return Mag(imie, hp=80, sila=5, inteligencja=20)
    else:
        return Gracz(imie, hp=100, sila=10, inteligencja=10)

postac1 = fabryka_postaci("Wojownik", "Conan")
postac2 = fabryka_postaci("Mag", "Gandalf")
print(postac1)
print(postac2)


# Zadanie 2
class Ekspert:
    def __init__(self, imie):
        self.imie = imie

    def przetwarzaj(self):
        return f"{self.imie} przetwarza dane..."


class System:
    def __init__(self):
        self.ekspert = Ekspert("AI_System")

    def uruchom_analize(self):
        return self.ekspert.przetwarzaj()


# Zadanie 3
class Notatka:
    def __init__(self, tresc):
        self.tresc = tresc

    def pokaz(self):
        return f"Notatka: {self.tresc}"


class FormatowanyTekst:
    def __init__(self, notatka):
        self.notatka = notatka

    def pokaz(self):
        return f">>> {self.notatka.pokaz()} <<<"


notatka = Notatka("Zrobic zakupy")
tekst = FormatowanyTekst(notatka)
print(tekst.pokaz())


# Zadanie 4
class StarySystem:
    def stare_api(self):
        return "Dane w starym formacie"


class NowySystem:
    def nowe_api(self):
        return {"dane": "aktualne", "typ": "slownik"}


class Adapter:
    def __init__(self, stary_system):
        self.stary_system = stary_system

    def nowe_api(self):
        dane = self.stary_system.stare_api()
        return {"dane": dane, "typ": "adapter"}


stary = StarySystem()
adapter = Adapter(stary)
print(adapter.nowe_api())


# Zadanie 5
class Płatnosc:
    def plat(self, kwota):
        pass


class PlatnoscKarta(Płatnosc):
    def plat(self, kwota):
        return f"Płatność kartą: {kwota} zł"


class PlatnoscPayPal(Płatnosc):
    def plat(self, kwota):
        return f"Płatność PayPal: {kwota} zł"


def dokonaj_transakcji(service_platnosci, kwota):
    return service_platnosci.plat(kwota)


platnosc_karta = PlatnoscKarta()
platnosc_paypal = PlatnoscPayPal()

print(dokonaj_transakcji(platnosc_karta, 100))
print(dokonaj_transakcji(platnosc_paypal, 200))


# Zadanie 6
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SerwisBazyDanych(metaclass=SingletonMeta):
    def __init__(self):
        self.status = "Połączony"

    def ping(self):
        return f"Serwis DB: {self.status}"


baza1 = SerwisBazyDanych()
baza2 = SerwisBazyDanych()
print(baza1 is baza2)
print(baza1.ping())


# Zadanie 7
class Subskrybent:
    def aktualizacja(self, tresc):
        print(f"Otrzymano powiadomienie: {tresc}")


class SerwisWiadomosci:
    def __init__(self):
        self.subskrybenci = []

    def subskrybuj(self, subskrybent):
        self.subskrybenci.append(subskrybent)

    def anuluj_subskrypcje(self, subskrybent):
        self.subskrybenci.remove(subskrybent)

    def powiadom_wszystkich(self, tresc):
        for subskrybent in self.subskrybenci:
            subskrybent.aktualizacja(tresc)


sub1 = Subskrybent()
sub2 = Subskrybent()
serwis = SerwisWiadomosci()

serwis.subskrybuj(sub1)
serwis.subskrybuj(sub2)

serwis.powiadom_wszystkich("Nowa wiadomość!")


# Zadanie 8
class Portfel:
    def __init__(self, pieniadze):
        self.pieniadze = pieniadze

    def ile_mam(self):
        return self.pieniadze


class Gracz:
    def __init__(self, imie, pieniadze):
        self.imie = imie
        self.portfel = Portfel(pieniadze)

    def zaplac(self, kwota):
        if self.portfel.ile_mam() >= kwota:
            self.portfel.pieniadze -= kwota
            return f"{self.imie} zapłacił {kwota} zł."
        else:
            return f"{self.imie} nie ma wystarczającej ilości pieniędzy."


gracz = Gracz("Jan", 150)
print(gracz.zaplac(50))
print(gracz.zaplac(120))
