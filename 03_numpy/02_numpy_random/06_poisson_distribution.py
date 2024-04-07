"""
Poisson Distribution merupakan Distribusi Diskrit.
    1. Ini memperkirakan berapa kali suatu peristiwa dapat terjadi dalam waktu tertentu.
    2. Misalnya, jika seseorang makan dua kali sehari, berapa peluang dia makan tiga kali?
    3. Ini memiliki dua parameter:
        - lam- rate atau jumlah kemunculan yang diketahui misalnya 2 untuk soal di atas.
        - size- Bentuk array yang dikembalikan.

Perbedaan Antara Distribusi Normal dan Poisson
    1. Distribusi normal bersifat kontinu sedangkan poisson bersifat diskrit.
    2. Namun kita dapat melihat bahwa mirip dengan binomial untuk distribusi poisson yang cukup besar akan menjadi serupa dengan distribusi normal dengan std dev dan mean tertentu.

Perbedaan Antara Distribusi Binomial dan Poisson
    1. Distribusi binomial hanya mempunyai dua kemungkinan hasil, sedangkan distribusi poisson mempunyai kemungkinan hasil yang tidak terbatas.
    2. Namun untuk distribusi binomial yang sangat besar ndan mendekati nol p hampir identik dengan distribusi poisson sehingga n * p hampir sama dengan lam.
"""
# Hasilkan distribusi acak 1x10 untuk kejadian 2
from numpy import random

x = random.poisson(lam=2, size=10)

print(x)

# Visualisasi Distribusi Poisson
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()

# Perbedaan Antara Distribusi Normal dan Poisson
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show()

# Perbedaan Antara Distribusi Binomial dan Poisson
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()