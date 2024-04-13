"""
1. Distribusi Zipf digunakan untuk mengambil sampel data berdasarkan hukum zipf.
2. Hukum Zipf: Dalam suatu kumpulan, suku persekutuan ke-n adalah 1/n kali suku terbanyak. Misalnya, kata paling umum ke-5 dalam bahasa Inggris muncul hampir 1/5 kali lebih sering daripada kata yang paling umum.
3. Ini memiliki dua parameter:
    a-      parameter distribusi.
    size-   Bentuk array yang dikembalikan.
"""
# Gambarkan contoh distribusi zipf dengan parameter distribusi 2 dengan ukuran 2x3
from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)

## Visualisasi Distribusi Zipf
# Ambil sampel 1000 poin tetapi plotkan hanya poin dengan nilai <10 untuk grafik yang lebih bermakna.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()

"""
Kode ini menghasilkan sampel acak dari distribusi Zipf dengan parameter a=2 dalam bentuk array dengan ukuran (2, 3). 
Distribusi Zipf adalah distribusi probabilitas diskrit yang sering digunakan untuk memodelkan fenomena yang melibatkan distribusi kejadian yang jarang dan memiliki ekor panjang.

Parameter a dalam distribusi Zipf adalah parameter bentuk (shape parameter), yang mengontrol kecondongan distribusi. Semakin besar nilai a, semakin curam distribusinya.

Dalam konteks aplikasi, distribusi Zipf sering digunakan dalam pemodelan frekuensi kata dalam teks, distribusi kekayaan dalam ekonomi, dan distribusi frekuensi dalam jaringan sosial.
"""