"""
1. Histogram adalah grafik yang menunjukkan distribusi frekuensi .
2. Ini adalah grafik yang menunjukkan jumlah observasi dalam setiap interval tertentu.
3. Buat Histogram
    - Di Matplotlib, kami menggunakan hist() fungsi untuk membuat histogram.
    - Fungsi tersebut hist() akan menggunakan array angka untuk membuat histogram, array tersebut dikirim ke fungsi sebagai argumen.
    - hist()akan membaca array dan menghasilkan histogram
"""
# Histogram sederhana
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()