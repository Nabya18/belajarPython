"""
Distribusi Chi Square
1. Distribusi Chi Square digunakan sebagai dasar untuk memverifikasi hipotesis.
2. Ini memiliki dua parameter:
    df-     (derajat kebebasan).
    size-   Bentuk array yang dikembalikan.
"""
# Buatlah contoh distribusi chi kuadrat dengan derajat kebebasan 2 dengan ukuran 2x3
from numpy import random

x = random.chisquare(df=2, size=(2, 3))

print(x)

## Visualisasi Distribusi Chi Kuadrat
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()

"""
Kode ini menghasilkan sampel acak dari distribusi chi-square dengan parameter df=2 dalam bentuk array dengan ukuran (2, 3). 
Distribusi chi-square adalah distribusi probabilitas yang muncul dalam teori probabilitas dan statistika, 
dan digunakan dalam berbagai analisis statistik.

Parameter df adalah derajat kebebasan (degree of freedom), yang mengontrol bentuk distribusi. 
Semakin besar nilai df, semakin "normal" distribusi chi-square tersebut, yaitu semakin mendekati distribusi normal.

Dalam konteks aplikasi, distribusi chi-square sering digunakan dalam uji statistik 
seperti uji chi-square untuk menguji independensi variabel dalam tabel kontingensi, 
atau dalam analisis regresi untuk menguji signifikansi variabel-variabel prediktor.
"""