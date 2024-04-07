"""
Uniform Distribution
    1. Digunakan untuk menggambarkan probabilitas di mana setiap peristiwa memiliki peluang yang sama untuk terjadi.
    2. Misalnya Pembuatan angka acak.
    3. Ini memiliki tiga parameter:
        a-      batas bawah - default 0 .0.
        b-      batas atas - default 1.0.
        size-   Bentuk array yang dikembalikan.


"""
# Buat sampel distribusi seragam 2x3
from numpy import random

x = random.uniform(size=(2, 3))

print(x)

# Visualisasi Distribusi Uniform
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000), hist=False)

plt.show()