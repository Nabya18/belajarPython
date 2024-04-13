"""
Distribusi eksponensial
1. Distribusi eksponensial digunakan untuk menggambarkan waktu hingga kejadian berikutnya, misalnya kegagalan/sukses, dll.
2. Ini memiliki dua parameter:
    scale-  kebalikan dari rate (lihat lam dalam distribusi poisson) defaultnya adalah 1.0.
    size-   Bentuk array yang dikembalikan.

Hubungan Antara Poisson dan Distribusi Eksponensial
    1. Distribusi Poisson berkaitan dengan jumlah kemunculan suatu peristiwa dalam suatu periode waktu,
    2. sedangkan distribusi eksponensial berkaitan dengan waktu antara peristiwa-peristiwa tersebut.
"""
# Gambarlah sampel untuk distribusi eksponensial skala 2.0 dengan ukuran 2x3
from numpy import random

x = random.exponential(scale=2, size=(2, 3))

print(x)

## Visualisasi Distribusi Eksponensial
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size=1000), hist=False)

plt.show()

"""
Kode ini menghasilkan sampel acak dari distribusi eksponensial dengan parameter scale=2 dalam bentuk array dengan ukuran (2, 3). 
Distribusi eksponensial adalah distribusi probabilitas yang digunakan untuk memodelkan waktu antara dua peristiwa yang terjadi secara independen dan secara konstan dalam waktu.

Parameter scale dalam distribusi eksponensial mengontrol "skala" atau "besaran" distribusi. Semakin besar nilai scale, semakin lambat distribusinya akan mengecil.

Dalam konteks aplikasi, distribusi eksponensial sering digunakan dalam pemodelan waktu tunggu, seperti waktu antara kedatangan pelanggan dalam antrian, 
waktu antara kegagalan mesin dalam analisis keandalan, atau waktu antara penyebaran partikel dalam fisika.
"""