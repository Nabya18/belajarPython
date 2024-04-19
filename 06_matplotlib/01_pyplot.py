"""
1. Sebagian besar utilitas Matplotlib terletak di bawah pyplot submodul, dan biasanya diimpor dengan plt alias
2. Pyplot adalah submodul dalam library Matplotlib di Python yang digunakan untuk membuat plot dan visualisasi data dalam berbagai format yang berbeda.
3. Fungsi-fungsi dalam pyplot digunakan untuk membuat figure, membuat plotting area, plot garis, menghias plot dengan label, dll.
4. Berikut adalah beberapa fungsi dasar yang sering digunakan dalam pyplot:
    - plt.plot(): Fungsi ini digunakan untuk membuat plot.
        Kita bisa memberikan dua array sebagai parameter, array pertama akan menjadi sumbu x dan array kedua akan menjadi sumbu y.
    - plt.show(): Fungsi ini digunakan untuk menampilkan plot yang telah dibuat.
        Biasanya dipanggil setelah semua plot dan dekorasi (seperti label dan judul) telah ditambahkan.
    - plt.xlabel(), plt.ylabel(): Fungsi ini digunakan untuk menambahkan label pada sumbu x dan y.
    - plt.title(): Fungsi ini digunakan untuk menambahkan judul pada plot.
    - plt.grid(): Fungsi ini digunakan untuk menambahkan grid pada plot.
    - plt.legend(): Fungsi ini digunakan untuk menambahkan legenda pada plot.
"""
# Gambarlah garis pada diagram dari posisi (0,0) ke posisi (6,250)
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()