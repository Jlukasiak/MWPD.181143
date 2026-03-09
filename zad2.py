import numpy as np

zadanie1 = np.arange(10)

zadanie1_float = zadanie1.astype(np.float32)

print("Tablica po zmianie na float32:")
print(zadanie1_float)

print(f"\nNowy typ danych (dtype): {zadanie1_float.dtype}")