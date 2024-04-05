"""
Searching Array
    1. Kita dapat mencari array untuk nilai tertentu, dan mengembalikan indeks yang cocok.
    2. Untuk mencari array, gunakan where() metode ini.

Pencarian Diurutkan
    1. Ada metode yang disebut searchsorted()yang melakukan pencarian biner dalam array,
    2. dan mengembalikan indeks di mana nilai yang ditentukan akan dimasukkan untuk mempertahankan urutan pencarian.
    3. Metode ini searchsorted()diasumsikan digunakan pada array yang diurutkan.

Cari dari sisi kanan
    Secara default, indeks paling kiri dikembalikan, tetapi kita dapat memberikan side='right'indeks paling kanan sebagai gantinya.

Berbagai Nilai
    Untuk mencari lebih dari satu nilai, gunakan array dengan nilai yang ditentukan.

"""
## contoh: Temukan indeks yang nilainya 4
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
"""
(array([3, 5, 6], dtype=int64),): Ini adalah bentuk output dari np.where(). Ini adalah tupel yang berisi array satu dimensi yang berisi indeks di mana kondisi terpenuhi.
Dalam hal ini, nilai 4 muncul di indeks 3, 5, dan 6 dalam array arr. Oleh karena itu, np.where(arr == 4) mengembalikan array satu dimensi yang berisi indeks 3, 5, dan 6.
dtype=int64 menunjukkan tipe data dari indeks yang dikembalikan adalah int64.i 4 ada di indeks 3, 5, dan 6 dalam array arr, sehingga hasilnya adalah (array([3, 5, 6], dtype=int64),).
"""

# Temukan indeks yang nilainya genap
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

# Temukan indeks yang nilainya ganjil
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)


## Pencarian diurutkan
# Temukan indeks di mana nilai 7 harus dimasukkan
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)
"""
Contoh yang dijelaskan: Angka 7 sebaiknya disisipkan pada indeks 1 agar urutannya tetap.
Metode ini memulai pencarian dari kiri dan mengembalikan indeks pertama dimana angka 7 tidak lagi lebih besar dari nilai berikutnya.
"""

# Temukan indeks di mana nilai 7 harus dimasukkan, dimulai dari kanan
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)

# Temukan indeks di mana nilai 2, 4, dan 6 harus dimasukkan
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)
"""
Penjelasan:
    Pertama, kita memiliki array arr yang sudah diurutkan: [1, 3, 5, 7].
    Kemudian, kita mencari indeks di mana nilai [2, 4, 6] harus disisipkan ke dalam array arr.
    Untuk nilai 2, indeks di mana nilai 2 harus disisipkan adalah 1 (setelah nilai 1 dan sebelum nilai 3).
    Untuk nilai 4, indeks di mana nilai 4 harus disisipkan adalah 2 (setelah nilai 3 dan sebelum nilai 5).
    Untuk nilai 6, indeks di mana nilai 6 harus disisipkan adalah 3 (setelah nilai 5 dan sebelum nilai 7).
    Oleh karena itu, hasilnya adalah [1 2 3], yang menunjukkan indeks-indeks di mana nilai-nilai tersebut harus disisipkan ke dalam array arr.
"""