"""
### Zadanie 2 — Filtrowanie i ranking sekwencji DNA

Plik `dane/sekwencje.txt` zawiera w każdym wierszu identyfikator i niepustą sekwencję DNA, rozdzielone spacją. Sekwencje zawierają wyłącznie wielkie litery A, T, G, C.

1. Wczytaj rekordy i dla każdego oblicz długość, liczbę tymin oraz procent GC.
2. Za pomocą `filter()` i lambdy pozostaw sekwencje o długości co najmniej 8 i GC od 40% do 60% włącznie.
3. Posortuj wybrane rekordy przez `sorted()` i lambdę: malejąco według GC, przy remisie rosnąco według identyfikatora. Sortuj na niezaokrąglonych wartościach.
4. Dla wszystkich sekwencji uzyskaj listę liczb tymin na dwa sposoby: `map()` z lambdą oraz listą składaną. Porównaj wyniki.
5. Zapisz ranking do `ranking_dna.txt`: identyfikator, sekwencja, długość, liczba T i GC z dwoma miejscami po przecinku. Jeżeli nie wybrano rekordów, zapisz informację o pustym rankingu.

**Kontrola:** wybrane rekordy w kolejności to `S03`, `S05`, `S01`, `S06`. Lista liczb tymin dla całego pliku to `[2, 4, 2, 0, 0, 3]`.

"""

f = open("sekwencje.txt","r")
dna_list = [i for i in f]
print(dna_list)

def cutN(s):
    if "\n" in s:
        return s[0:-1]
    else: 
        return s 
def getHeader(s):
    return s[0:3]
def getBody(s):
    return s[4:len(s)]

dna_list = [cutN(s) for s in dna_list]
print(dna_list)

dna_headers = [getHeader(s) for s in dna_list]
dna_body = [getBody(s) for s in dna_list]
print(dna_headers)
print(dna_body)

dna_length = [len(i) for i in dna_body]
print(dna_length)

T_count = [s.count("T") for s in dna_body]
print(T_count)

GC_percent = [100*(s.count("G") + s.count("C"))/len(s) for s in dna_body]
print(GC_percent)

filtered_seq = list(filter(lambda s: len(s) >= 8 and 40 <= 100*(s.count("G") + s.count("C"))/len(s) and
                           60 >= 100*(s.count("G") + s.count("C"))/len(s),dna_body))

print(filtered_seq)
sort_key = zip(GC_percent,dna_headers)

