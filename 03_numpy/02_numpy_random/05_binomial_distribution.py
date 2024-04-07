"""
Distribusi Binomial
    1. Distribusi Binomial merupakan Distribusi Diskrit .
    2. Ini menggambarkan hasil skenario biner, misalnya pelemparan koin, baik kepala atau ekor.
    3. Ini memiliki tiga parameter:
        n- jumlah percobaan.
        p- probabilitas terjadinya setiap percobaan (misalnya untuk pelemparan koin masing-masing 0,5).
        size- Bentuk array yang dikembalikan.

Distribusi Diskrit: Distribusi didefinisikan pada rangkaian kejadian yang terpisah, misalnya hasil pelemparan koin bersifat diskrit karena hanya dapat berupa kepala atau ekor,
sedangkan tinggi badan orang bersifat kontinu karena dapat berupa 170, 170.1, 170.11 dan seterusnya.


Perbedaan Distribusi Normal dan Binomial
    1. Perbedaan utamanya adalah distribusi normal bersifat kontinu sedangkan binomial bersifat diskrit
    2. jika titik datanya cukup maka akan sangat mirip dengan distribusi normal dengan lokasi dan skala tertentu.
"""
# Diberikan 10 percobaan lempar koin menghasilkan 10 titik data
from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)

# Visualisasi Distribusi Binomial
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()
"""
random.binomial(n=10, p=0.5, size=1000) menghasilkan 1000 sampel dari distribusi binomial dengan parameter n=10 (jumlah percobaan) dan p=0.5 (probabilitas keberhasilan).

sns.distplot() digunakan untuk membuat plot distribusi. 
Argumen hist=True mengindikasikan bahwa histogram harus digunakan untuk menampilkan distribusi data, 
sedangkan kde=False menonaktifkan plot Kernel Density Estimation (KDE).

plt.show() digunakan untuk menampilkan plot.
"""

# Perbedaan Distribusi Normal dan Binomial
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()