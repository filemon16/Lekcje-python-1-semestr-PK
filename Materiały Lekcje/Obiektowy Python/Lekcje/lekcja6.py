# Zadanie 1
import re

def znajdz_ip_i_status(sciezka_pliku):
    with open(sciezka_pliku, 'r') as f:
        tresc = f.read()

    wzorzec_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    wzorzec_status = r'" \d{3} '

    adresy_ip = re.findall(wzorzec_ip, tresc)
    kody_statusu = [status.strip().strip('"') for status in re.findall(wzorzec_status, tresc)]

    return adresy_ip, kody_statusu


# Zadanie 2
from datetime import datetime

def analizuj_czas_logow(sciezka_pliku):
    with open(sciezka_pliku, 'r') as f:
        tresc = f.read()

    wzorzec_daty = r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
    daty_str = re.findall(wzorzec_daty, tresc)

    if not daty_str:
        return None

    format_daty = '%d/%b/%Y:%H:%M:%S'
    daty = [datetime.strptime(d, format_daty) for d in daty_str]

    return max(daty) - min(daty)


# Zadanie 3
def znajdz_wszystkie_adresy_mailowe(sciezka_pliku):
    with open(sciezka_pliku, 'r') as f:
        tresc = f.read()

    wzorzec = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(wzorzec, tresc)


# Zadanie 4
def znajdz_numery_telefonow(plik_tekstowy):
    with open(plik_tekstowy, 'r') as f:
        tresc = f.read()

    wzorzec = r'\+?\d{2}[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{3}|\(\d{3}\)\s?\d{3}-\d{4}'
    return re.findall(wzorzec, tresc)


# Zadanie 5
def popraw_nieveidlome_linki(sciezka_pliku):
    with open(sciezka_pliku, 'r') as f:
        tresc = f.read()

    wzorzec = r'https?://(?:www\.)?([a-zA-Z0-9./\-_]+)'
    poprawione = re.sub(wzorzec, r'<a href="http://\1">\1</a>', tresc)
    return poprawione


# Zadanie 6
def znajdz_komentarze_html(sciezka_pliku):
    with open(sciezka_pliku, 'r') as f:
        tresc = f.read()

    wzorzec = r'<!--(.*?)-->'
    return re.findall(wzorzec, tresc, re.DOTALL)


# Zadanie 7
def znajdz_ceny_towarow(sciezka_pliku):
    with open(sciezka_pliku, 'r') as f:
        tresc = f.read()

    wzorzec = r'(\d+(?:\.\d{2})?)\s*(?:zl|zł|PLN)'
    znalezione = re.findall(wzorzec, tresc)
    return [float(cena) for cena in znalezione]


# Zadanie 8
def znajdz_pelne_daty(sciezka_pliku):
    with open(sciezka_pliku, 'r') as f:
        tresc = f.read()

    wzorzec = r'\b\d{1,2}\.\d{1,2}\.\d{4}\b|\b\d{4}-\d{2}-\d{2}\b|\b\d{1,2}/\d{1,2}/\d{4}\b'
    return re.findall(wzorzec, tresc)
