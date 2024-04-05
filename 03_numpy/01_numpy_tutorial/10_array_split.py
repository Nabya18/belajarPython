"""
Splitting Array
    1. Pemisahan adalah kebalikan dari operasi Penggabungan.
    2. Penggabungan menggabungkan beberapa array menjadi satu dan Pemisahan memecah satu array menjadi beberapa.
    3. Kami menggunakannya array_split()untuk memisahkan array, kami meneruskannya ke array yang ingin kami bagi dan jumlah pemisahannya.

Jika array memiliki elemen lebih sedikit dari yang dibutuhkan, array akan menyesuaikan dari akhir.

metode split() tidak akan menyesuaikan elemen ketika elemen kurang dalam array
array_split() berfungsi dengan baik tetapi split()a kan gagal.

Dibagi Menjadi Array
    1. array_split() metode ini adalah larik yang berisi masing-masing pemisahan sebagai larik.
    2. Jika Kita membagi array menjadi 3 array, Kita dapat mengaksesnya dari hasil sama seperti elemen array lainnya

Memisahkan Array 2-D
    Gunakan array_split()metode ini, masukkan array yang ingin Kita bagi dan jumlah pemisahan yang ingin Kita lakukan.

Solusi alternatif menggunakan hsplit()kebalikan dari hstack()
Catatan: Alternatif serupa untuk vstack()dan dstack()tersedia sebagai vsplit()dan dsplit().
"""

## contoh: Bagi array menjadi 3 bagian
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
"""
Catatan: Nilai yang dikembalikan adalah daftar yang berisi tiga array.
"""

## contoh: Bagi array menjadi 4 bagian
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)

## Akses array yang dipisahkan
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])


## Memisahkan Array 2-D
# Pisahkan larik 2D menjadi tiga larik 2D.
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

# Pisahkan larik 2D menjadi tiga larik 2D
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)

# Contoh di bawah ini juga mengembalikan tiga array 2-D, tetapi array tersebut dibagi sepanjang baris (sumbu=1).
# Pisahkan larik 2D menjadi tiga larik 2D sepanjang baris
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

# Gunakan hsplit() metode ini untuk membagi larik 2D menjadi tiga larik 2D sepanjang baris.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)