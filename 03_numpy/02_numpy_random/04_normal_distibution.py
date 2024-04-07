"""
Normal (Gaussian) Distribution
    1. Distribusi Normal adalah salah satu distribusi yang paling penting.
    2. Distribusi ini juga disebut Distribusi Gaussian yang diambil dari nama matematikawan Jerman Carl Friedrich Gauss.
    3. Ini sesuai dengan distribusi probabilitas dari banyak peristiwa, misalnya. Skor IQ, Detak Jantung, dll.
    4. Gunakan random.normal()cara tersebut untuk mendapatkan Distribusi Data Normal.

Ini memiliki tiga parameter:
    1. loc- (Mean) dimana puncak loncengnya berada.
    2. scale- (Standard Deviation) seberapa datar seharusnya distribusi grafik.
    3. size- Bentuk array yang dikembalikan.

Catatan: Kurva Distribusi Normal disebut juga Kurva Lonceng karena kurvanya berbentuk lonceng.
"""
# Hasilkan distribusi normal acak ukuran 2x3
from numpy import random

x = random.normal(size=(2, 3))

print(x)


# Hasilkan distribusi normal acak berukuran 2x3 dengan mean 1 dan deviasi standar 2
x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)


## Visualisasi Distribusi Normal
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show()