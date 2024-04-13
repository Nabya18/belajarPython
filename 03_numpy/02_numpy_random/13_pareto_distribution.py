"""
Distribusi Pareto
1. Distribusi yang mengikuti hukum Pareto yaitu distribusi 80-20 (20% faktor menyebabkan 80% hasil).
2. Ini memiliki dua parameter:
    a-      parameter bentuk.
    size-   Bentuk array yang dikembalikan.



"""
# Buatlah contoh distribusi pareto berbentuk 2 dengan ukuran 2x3
from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)

## Visualisasi Distribusi Pareto
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()

"""
Kode yang Kita berikan menghasilkan sampel acak dari distribusi Pareto dengan parameter a=2 dalam bentuk array dengan ukuran (2, 3). 
Ini berarti Kita membuat array 2 dimensi dengan 2 baris dan 3 kolom, di mana setiap elemen dari array adalah sampel acak dari distribusi Pareto dengan parameter a=2.

Dalam distribusi Pareto, parameter a mengontrol bentuk distribusi. Semakin besar nilai a, semakin cepat ekor distribusi mengecil. 
Dalam kasus ini, karena a=2, ekor distribusi akan mengecil lebih lambat daripada jika a lebih besar.

Dalam konteks aplikasi, distribusi Pareto sering digunakan untuk mewakili fenomena di mana beberapa elemen memiliki dampak yang sangat besar, 
sementara sebagian besar memiliki dampak yang kecil. Misalnya, distribusi pendapatan sering kali dapat dijelaskan menggunakan distribusi Pareto, 
di mana sebagian kecil orang memiliki sebagian besar pendapatan.
"""