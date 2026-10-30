import copy


# Funkcja zwracająca za każdym razem świeże dane
def utworz_dane():
    return [
        {"nazwa": "A", "pomiary": [10, 12, 14]},
        {"nazwa": "B", "pomiary": [20, 22, 24]},
    ]


# Funkcja wyświetlająca dwie struktury
def pokaz_struktury(oryginal, wariant):
    print("Oryginał:", oryginal)
    print("Wariant: ", wariant)
    print()


# Funkcja wykonująca trzy modyfikacje
def modyfikuj(oryginal, wariant):
    print("Stan początkowy:")
    pokaz_struktury(oryginal, wariant)

    # Zmiana nazwy pierwszej próbki
    wariant[0]["nazwa"] = "A_mod"

    print("Po zmianie nazwy:")
    pokaz_struktury(oryginal, wariant)

    # Zwiększenie pierwszego pomiaru o 100
    wariant[0]["pomiary"][0] += 100

    print("Po zwiększeniu pierwszego pomiaru:")
    pokaz_struktury(oryginal, wariant)

    # Dodanie nowej próbki
    wariant.append({
        "nazwa": "C",
        "pomiary": [30, 32, 34]
    })

    print("Po dodaniu próbki C:")
    pokaz_struktury(oryginal, wariant)


# Sprawdzanie tożsamości obiektów
def sprawdz_tozsamosc(oryginal, wariant):
    print("Sprawdzanie tożsamości obiektów:")

    print(
        "Listy zewnętrzne:",
        oryginal is wariant
    )

    print(
        "Pierwsze słowniki:",
        oryginal[0] is wariant[0]
    )

    print(
        "Listy pomiarów:",
        oryginal[0]["pomiary"] is wariant[0]["pomiary"]
    )

    print()


# 1. Doświadczenie z przypisaniem
print("=" * 50)
print("DOŚWIADCZENIE 1 - PRZYPISANIE")
print("=" * 50)

oryginal = utworz_dane()
wariant = oryginal

modyfikuj(oryginal, wariant)
sprawdz_tozsamosc(oryginal, wariant)


# 2. Doświadczenie z copy.copy()
print("=" * 50)
print("DOŚWIADCZENIE 2 - COPY.COPY()")
print("=" * 50)

oryginal = utworz_dane()
wariant = copy.copy(oryginal)

modyfikuj(oryginal, wariant)
sprawdz_tozsamosc(oryginal, wariant)


# 3. Doświadczenie z copy.deepcopy()
print("=" * 50)
print("DOŚWIADCZENIE 3 - COPY.DEEPCOPY()")
print("=" * 50)

oryginal = utworz_dane()
wariant = copy.deepcopy(oryginal)

modyfikuj(oryginal, wariant)
sprawdz_tozsamosc(oryginal, wariant)


# 4. Dwa niezależne scenariusze
print("=" * 50)
print("DOŚWIADCZENIE 4 - NIEZALEŻNE SCENARIUSZE")
print("=" * 50)

oryginal = utworz_dane()

scenariusz_plus = copy.deepcopy(oryginal)
scenariusz_minus = copy.deepcopy(oryginal)

# Zwiększenie pomiarów o 10%
for probka in scenariusz_plus:
    probka["pomiary"] = [
        pomiar * 1.10 for pomiar in probka["pomiary"]
    ]

# Odjęcie 2 od każdego pomiaru
for probka in scenariusz_minus:
    probka["pomiary"] = [
        pomiar - 2 for pomiar in probka["pomiary"]
    ]


# Funkcja obliczająca średnią
def srednia(pomiary):
    return sum(pomiary) / len(pomiary)


# 5. Zestawienie wyników za pomocą zip()
print("\nTABELA ŚREDNICH")
print("-" * 75)

print(
    f"{'Próbka':<12}"
    f"{'Oryginał':<15}"
    f"{'Scenariusz +10%':<20}"
    f"{'Scenariusz -2':<15}"
)

print("-" * 75)

tabela = []

for org, plus, minus in zip(
    oryginal, scenariusz_plus, scenariusz_minus
):
    srednia_org = srednia(org["pomiary"])
    srednia_plus = srednia(plus["pomiary"])
    srednia_minus = srednia(minus["pomiary"])

    tabela.append((
        org["nazwa"],
        srednia_org,
        srednia_plus,
        srednia_minus
    ))

    print(
        f"{org['nazwa']:<12}"
        f"{srednia_org:<15.2f}"
        f"{srednia_plus:<20.2f}"
        f"{srednia_minus:<15.2f}"
    )


# Kontrola wyników
assert tabela[0][1:] == (12.0, 13.2, 10.0)
assert tabela[1][1:] == (22.0, 24.2, 20.0)

print("\nKontrola średnich zakończona poprawnie.")


# Sprawdzenie, czy oryginał pozostał bez zmian
print("\nOryginał po wykonaniu scenariuszy:")
print(oryginal)


# 6. Zapis raportu do pliku
with open("raport_kopie.txt", "w", encoding="utf-8") as plik:

    plik.write("RAPORT - KOPIOWANIE OBIEKTÓW W PYTHONIE\n")
    plik.write("=" * 55 + "\n\n")

    plik.write("1. PRZYPISANIE\n")
    plik.write(
        "Przypisanie nie tworzy nowego obiektu. "
        "Oryginal i wariant wskazują na tę samą listę.\n\n"
    )

    plik.write("2. KOPIA PŁYTKA - copy.copy()\n")
    plik.write(
        "Kopia płytka tworzy nową listę zewnętrzną, "
        "ale jej elementy nadal wskazują na te same słowniki "
        "i listy pomiarów.\n"
    )
    plik.write(
        "Zmiana nazwy i pomiaru jest widoczna w oryginale. "
        "Dodanie próbki C do wariantu nie wydłuża oryginału.\n\n"
    )

    plik.write("3. KOPIA GŁĘBOKA - copy.deepcopy()\n")
    plik.write(
        "Kopia głęboka tworzy niezależną strukturę. "
        "Zmiany nazwy, pomiarów i dodanie próbki C "
        "nie wpływają na oryginał.\n\n"
    )

    plik.write("4. NIEZALEŻNE SCENARIUSZE\n")
    plik.write(
        "Utworzono dwa scenariusze za pomocą deepcopy().\n"
        "Pierwszy zwiększa wszystkie pomiary o 10%.\n"
        "Drugi odejmuje 2 od każdego pomiaru.\n"
        "Oryginalne dane nie zostały zmienione.\n\n"
    )

    plik.write("5. TABELA ŚREDNICH\n")
    plik.write("-" * 75 + "\n")

    plik.write(
        f"{'Próbka':<12}"
        f"{'Oryginał':<15}"
        f"{'Scenariusz +10%':<20}"
        f"{'Scenariusz -2':<15}\n"
    )

    plik.write("-" * 75 + "\n")

    for nazwa, org, plus, minus in tabela:
        plik.write(
            f"{nazwa:<12}"
            f"{org:<15.2f}"
            f"{plus:<20.2f}"
            f"{minus:<15.2f}\n"
        )

    plik.write("\n6. WNIOSKI\n")
    plik.write("-" * 55 + "\n")

    plik.write(
        "Przypisanie powoduje współdzielenie całego obiektu.\n"
    )

    plik.write(
        "copy.copy() tworzy nową listę zewnętrzną, "
        "ale nie kopiuje rekurencyjnie jej elementów.\n"
    )

    plik.write(
        "copy.deepcopy() tworzy niezależną kopię całej struktury.\n"
    )

    plik.write(
        "Operator is pozwala sprawdzić, czy dwie zmienne "
        "wskazują na ten sam obiekt.\n"
    )

print("\nRaport zapisano do pliku raport_kopie.txt")
