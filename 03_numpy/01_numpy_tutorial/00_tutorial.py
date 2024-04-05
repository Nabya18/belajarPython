"""
1. NumPy adalah Library Python yang digunakan untuk bekerja dengan array.
2. NumPy memiliki fungsi untuk bekerja dalam domain aljabar linier, transformasi fourier, dan matriks.
3. NumPy adalah singkatan dari Python Numerik yang dibuat pada tahun 2005 oleh Travis Oliphant.
4. Objek array di NumPy disebut ndarray, ia menyediakan banyak fungsi pendukung yang membuat pengerjaannya menjadi ndarray sangat mudah.
5. NumPy biasanya diimpor dengan np alias.
6. alias: Dalam Python alias adalah nama alternatif untuk merujuk pada hal yang sama.
7. type(): Fungsi bawaan Python ini memberi tahu kita jenis objek yang diteruskan ke sana. Seperti pada kode di atas, ini menunjukkan bahwa itu arra dalah numpy.ndarraytipe.
"""

# contoh
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


# Memeriksa Versi NumPy
print(np.__version__)