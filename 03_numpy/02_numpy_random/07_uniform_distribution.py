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

"""
Kode ini menggunakan distribusi seragam (uniform) untuk menghasilkan sampel acak dari bilangan acak dalam interval [0, 1) dalam bentuk array dengan ukuran (2, 3). 
Distribusi seragam adalah distribusi probabilitas di mana setiap nilai dalam rentang yang diberikan memiliki probabilitas yang sama untuk muncul.

Dalam konteks ini, random.uniform() menghasilkan array dua dimensi dengan ukuran 2 baris dan 3 kolom, di mana setiap elemen array adalah bilangan acak yang diambil secara acak dan seragam dari interval [0, 1).

Hasilnya adalah array yang berisi bilangan acak antara 0 dan 1, di mana probabilitas munculnya setiap bilangan dalam rentang tersebut adalah sama.


Dalam konteks aplikasi, distribusi seragam (uniform) dapat digunakan untuk berbagai tujuan, di antaranya:
    1. Simulasi Komputer: Distribusi seragam sering digunakan dalam simulasi komputer untuk menghasilkan bilangan acak yang merata dari interval tertentu. Misalnya, dalam simulasi fisika atau permainan komputer, distribusi seragam digunakan untuk menghasilkan posisi atau kecepatan awal objek dalam ruang.
    2. Pemilihan Sampel Acak: Ketika memilih sampel acak dari suatu populasi, distribusi seragam dapat digunakan untuk memastikan bahwa setiap anggota populasi memiliki probabilitas yang sama untuk dipilih. Ini penting dalam metode sampling acak sederhana.
    3. Generasi Kunci Enkripsi: Dalam kriptografi, distribusi seragam digunakan dalam pembangkitan kunci enkripsi yang kuat. Memilih bilangan acak dari distribusi seragam dapat memberikan keamanan yang baik dalam enkripsi data.
    4. Pemodelan Proporsi: Dalam beberapa kasus, kita ingin memodelkan fenomena di mana setiap nilai dalam suatu rentang memiliki probabilitas yang sama untuk muncul. Misalnya, dalam analisis pemodelan, kita mungkin ingin memodelkan distribusi tingkat kehadiran di sebuah acara, dengan asumsi bahwa setiap kemungkinan tingkat kehadiran memiliki probabilitas yang sama.
    5. Pemrosesan Gambar dan Grafika: Dalam pemrosesan gambar dan grafika komputer, distribusi seragam dapat digunakan untuk menghasilkan warna atau titik acak di dalam gambar.
"""