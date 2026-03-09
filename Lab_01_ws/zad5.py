import numpy as np

# Tworzymy kostkę 3x3x3 z wartościami od 1 do 27
# Zgodnie z punktem 2.2 z pliku
kostka = np.arange(1, 28).reshape(3, 3, 3)

print("Pełna kostka 3x3x3:")
print(kostka)
print("-" * 30)

widok_y1 = kostka[:, 1, :]

print("Elementy dla y = 1 (środkowe wiersze każdej warstwy):")
print(widok_y1)
print("-" * 30)

widok_z1_z3 = kostka[[0, 2], :, :]

print("Elementy dla z = 1 oraz z = 3 (pierwsza i ostatnia warstwa/plaster):")
print(widok_z1_z3)