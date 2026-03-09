import numpy as np


wykladniki = np.arange(2, 17)

zadanie_potegi = 2 ** wykladniki
print("Kolejne potęgi liczby 2 (wykładniki 2-16):")
print(zadanie_potegi)

print(f"\nKształt tablicy: {zadanie_potegi.shape}")
print(f"Typ danych: {zadanie_potegi.dtype}")