import numpy as np
from timeit import timeit

setup1 = "l = list(range(10000))"
stmt1 = """
for i in range(len(l)):
    l[i] = l[i] * 2
"""

stmt2 = "[x * 2 for x in range(10000)]"


setup3 = "import numpy as np"
stmt3 = "np.arange(10000) * 2"


t1 = timeit(stmt=stmt1, setup=setup1, number=1000)
t2 = timeit(stmt=stmt2, number=1000)
t3 = timeit(stmt=stmt3, setup=setup3, number=1000)

print(f"Pętla for: {t1:.4f} s")
print(f"List comprehension: {t2:.4f} s")
print(f"NumPy: {t3:.4f} s")