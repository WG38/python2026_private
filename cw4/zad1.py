"""
### Zadanie 1 — Rekurencyjna analiza zagnieżdżonych danych

Dane pomiarowe zapisano jako listę o zmiennej głębokości zagnieżdżenia:

```python
dane = [4, [7, [2, 9]], [], [-3, [5]], 6]
```

1. Napisz rekurencyjną funkcję `splaszcz(dane)`, zwracającą nową, płaską listę liczb w pierwotnej kolejności. Obsłuż także puste listy i nie zmieniaj danych źródłowych.
2. Napisz rekurencyjną funkcję `glebokosc(dane)`. Przyjmij, że pusta lista i lista samych liczb mają głębokość 1; każda lista wewnętrzna zwiększa głębokość o 1. Przykładowo `[1, [2]]` ma głębokość 2.
3. Dla spłaszczonych danych wyznacz liczbę pomiarów, sumę, średnią, minimum i maksimum. Zakładamy, że cały zestaw zawiera co najmniej jedną liczbę.
4. Listą składaną wybierz dodatnie pomiary i oblicz ich kwadraty.
5. Zapisz wyniki do `raport_zagniezdzenia.txt`. W komentarzu wskaż warunki bazowe obu funkcji i wyjaśnij, dlaczego kończą działanie.

**Kontrola:** płaska lista to `[4, 7, 2, 9, -3, 5, 6]`, suma wynosi `30`, a głębokość `3`. Sprawdź też `splaszcz([])` i `glebokosc([])`.

"""

dane = [4, [7, [2, 9]], [], [-3, [5]], 6]


def splaszcz(dane):
    return_list = []
    for i in range(0,len(dane)):
        if isinstance(dane[i],list):
            return_list.extend(splaszcz(dane[i]))
        else:
            return_list.append(dane[i])
    return return_list 

def glebokosc(dane):
    depth_list = [0 for i in range(0,len(dane))]
    for i in range(0,len(dane)):
        if isinstance(dane[i],list):
            depth_list[i] += glebokosc(dane[i])
        else: 
            depth_list[i] += 1 
    return max(depth_list) 


splaszczone_dane = splaszcz(dane)
liczba = len(splaszczone_dane)
suma = sum(splaszczone_dane)
avg = suma/liczba 
n_min = min(splaszczone_dane)
n_max = max(splaszczone_dane)

positivesquared_list = [n**2 for n in splaszczone_dane if n > 0]

print(liczba)
print(suma)
print(avg)
print(n_min)
print(n_max)
print(splaszcz(dane))
print(positivesquared_list)

    

