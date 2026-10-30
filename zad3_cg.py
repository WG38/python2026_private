import sys
import time


# 1. Funkcja wykorzystująca pętlę i append()
def metoda_append(liczby):
    wynik = []
    for x in liczby:
        if x % 2 == 0:
            wynik.append(x ** 2)
    return wynik


# 2. Funkcja wykorzystująca listę składaną
def metoda_list_comprehension(liczby):
    return [x ** 2 for x in liczby if x % 2 == 0]


# 3. Funkcja wykorzystująca filter() i map()
def metoda_map_filter(liczby):
    return list(map(lambda x: x ** 2,
                    filter(lambda x: x % 2 == 0, liczby)))


# Sprawdzenie argumentów programu
if len(sys.argv) != 3:
    print("Użycie: python3 zadanie_04.py n powtorzenia")
    sys.exit(1)

n = int(sys.argv[1])
powtorzenia = int(sys.argv[2])

if n <= 0 or powtorzenia <= 0:
    print("Argumenty muszą być dodatnimi liczbami całkowitymi.")
    sys.exit(1)


# Utworzenie wspólnego obiektu range(n)
zakres = range(n)


# Sprawdzenie zgodności wyników
wynik_append = metoda_append(zakres)
wynik_comprehension = metoda_list_comprehension(zakres)
wynik_map = metoda_map_filter(zakres)

assert wynik_append == wynik_comprehension
assert wynik_append == wynik_map

print("Wyniki wszystkich metod są identyczne.")


# Pomiar czasu wykonywania funkcji
def zmierz_czas(funkcja, dane, powtorzenia):
    czasy = []

    for _ in range(powtorzenia):
        start = time.perf_counter()
        wynik = funkcja(dane)
        koniec = time.perf_counter()

        czasy.append(koniec - start)

    minimum = min(czasy)
    srednia = sum(czasy) / len(czasy)

    return minimum, srednia


metody = [
    ("append()", metoda_append),
    ("Lista skladana", metoda_list_comprehension),
    ("map() + filter()", metoda_map_filter)
]

wyniki_pomiarow = []

for nazwa, funkcja in metody:
    minimum, srednia = zmierz_czas(
        funkcja, zakres, powtorzenia
    )

    wyniki_pomiarow.append((nazwa, minimum, srednia))


# Wyświetlenie wyników pomiarów
print("\nCzasy wykonywania:")
print(f"Liczba elementów n: {n}")
print(f"Liczba powtórzeń: {powtorzenia}")

for nazwa, minimum, srednia in wyniki_pomiarow:
    print(f"\n{nazwa}:")
    print(f"  Minimum: {minimum:.6f} s")
    print(f"  Średnia: {srednia:.6f} s")


# 4. Pomiar rozmiaru listy, krotki i iteratora map()
krotka = tuple(wynik_append)

iterator_map = map(
    lambda x: x ** 2,
    filter(lambda x: x % 2 == 0, zakres)
)

import sys as system

rozmiar_listy = system.getsizeof(wynik_append)
rozmiar_krotki = system.getsizeof(krotka)
rozmiar_iteratora = system.getsizeof(iterator_map)

print("\nRozmiary obiektów:")
print(f"Lista: {rozmiar_listy} bajtów")
print(f"Krotka: {rozmiar_krotki} bajtów")
print(f"Iterator map(): {rozmiar_iteratora} bajtów")


# 5. Dwukrotna konwersja tego samego iteratora na listę
iterator = map(
    lambda x: x ** 2,
    filter(lambda x: x % 2 == 0, zakres)
)

lista1 = list(iterator)
lista2 = list(iterator)

print("\nDwukrotna konwersja iteratora:")
print(f"Długość pierwszej listy: {len(lista1)}")
print(f"Długość drugiej listy: {len(lista2)}")


# 6. Zapis wyników do pliku
with open("porownanie_metod.txt", "w", encoding="utf-8") as plik:

    plik.write("PORÓWNANIE METOD OBLICZANIA KWADRATÓW\n")
    plik.write("=" * 45 + "\n\n")

    plik.write(f"Liczba elementów n: {n}\n")
    plik.write(f"Liczba powtórzeń: {powtorzenia}\n")
    plik.write(f"Liczba wynikowych elementów: {len(wynik_append)}\n")

    plik.write("\nCZASY WYKONYWANIA\n")
    plik.write("-" * 45 + "\n")

    for nazwa, minimum, srednia in wyniki_pomiarow:
        plik.write(f"\n{nazwa}:\n")
        plik.write(f"Minimum: {minimum:.6f} s\n")
        plik.write(f"Średnia: {srednia:.6f} s\n")

    plik.write("\nROZMIARY OBIEKTÓW\n")
    plik.write("-" * 45 + "\n")
    plik.write(f"Lista: {rozmiar_listy} bajtów\n")
    plik.write(f"Krotka: {rozmiar_krotki} bajtów\n")
    plik.write(f"Iterator map(): {rozmiar_iteratora} bajtów\n")

    plik.write("\nDWUKROTNA KONWERSJA ITERATORA\n")
    plik.write("-" * 45 + "\n")
    plik.write(f"Długość pierwszej listy: {len(lista1)}\n")
    plik.write(f"Długość drugiej listy: {len(lista2)}\n")

    plik.write("\nWNIOSKI\n")
    plik.write("-" * 45 + "\n")

    plik.write(
        "Wszystkie trzy metody zwracają identyczne wyniki.\n"
    )

    plik.write(
        "Różnice w czasie wykonywania wynikają ze sposobu "
        "realizacji poszczególnych operacji.\n"
    )

    plik.write(
        "Nie można z góry założyć, która metoda będzie "
        "najszybsza. Wynik zależy między innymi od wersji "
        "Pythona i środowiska wykonania.\n"
    )

    plik.write(
        "sys.getsizeof() zwraca rozmiar samego obiektu, "
        "a nie całkowitą pamięć zajmowaną przez wszystkie "
        "obiekty powiązane z obliczeniami.\n"
    )

    plik.write(
        "Iterator jest jednorazowy. Po wykorzystaniu jego "
        "elementów kolejne wywołanie list() zwraca pustą listę.\n"
    )

print("\nWyniki zapisano do pliku porownanie_metod.txt")
