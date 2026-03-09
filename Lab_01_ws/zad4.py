import numpy as np

macierz = np.arange(1, 26).reshape(5, 5)

print("Macierz bazowa:")
print(macierz)
print("-" * 20)


ostatnia_wartosc = macierz[-1, -1]
print(f"Ostatnia wartość: {ostatnia_wartosc}")


druga_kolumna = macierz[:, 1]
print(f"Druga kolumna: {druga_kolumna}")

trzeci_wiersz = macierz[2, :]
print(f"Trzeci wiersz: {trzeci_wiersz}")


przekatna = np.diag(macierz)
print(f"Główna przekątna: {przekatna}")


wycinek = macierz[1:3, 3:5]
print("Wycinek 2x2 (9, 10, 14, 15):")
print(wycinek)