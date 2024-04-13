"""
1. Distribusi Rayleigh digunakan dalam pemrosesan sinyal.
2. Ini memiliki dua parameter:
    scale-  (deviasi standar) menentukan seberapa datar distribusi akan menjadi default 1.0).
    size-   Bentuk array yang dikembalikan.

Persamaan Antara Distribusi Rayleigh dan Chi Square
    Pada satuan stddev dan 2 derajat kebebasan rayleigh dan chi square mewakili distribusi yang sama.
"""
# Gambarlah sampel distribusi rayleigh skala 2 dengan ukuran 2x3
from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)

## Visualisasi Distribusi Rayleigh
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()

"""
Kode ini menghasilkan sampel acak dari distribusi Rayleigh dengan parameter scale=2 dalam bentuk array dengan ukuran (2, 3). 
Distribusi Rayleigh adalah distribusi probabilitas yang digunakan untuk mewakili magnitudo dari jumlah vektor dua dimensi yang memiliki komponen gaussian independen dan identik.

Parameter scale dalam distribusi Rayleigh mengontrol "skala" atau "besaran" distribusi. Semakin besar nilai scale, semakin besar distribusinya secara keseluruhan.

Dalam konteks aplikasi, distribusi Rayleigh sering digunakan dalam komunikasi nirkabel, terutama untuk mewakili kekuatan sinyal yang terdeteksi.
"""