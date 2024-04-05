"""
Slicing Arrays => mengambil elemen dari satu indeks tertentu ke indeks lain.
    1. [start:end]
    2. [start:end:step]
        start dianggap 0
    3. Slicing Negatif => Gunakan operator minus untuk merujuk ke indeks dari akhir
    4. Step => untuk menentukan langkah slicing
    5. Mengiris Array 2-D
        Catatan: Ingatlah bahwa elemen kedua memiliki indeks 1.
"""
# slicing elemen dari indeks 1 ke indeks 5 dari larik berikut
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

# slicing  elemen dari indeks 4 hingga akhir array
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

# slicing elemen dari awal hingga indeks 4 (tidak termasuk)
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])


## Slicing Negatif
# Slicing dari indeks 3 dari ujung ke indeks 1 dari akhir
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1]) # 7 tidak termasuk


## Step
# Kembalikan setiap elemen lainnya dari indeks 1 ke indeks 5
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

# Kembalikan setiap elemen lain dari seluruh array
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])


## Slicing Array 2-D
# Dari elemen kedua, potong elemen dari indeks 1 ke indeks 4 (tidak termasuk)
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

# Dari kedua elemen, kembalikan indeks 2
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])

"""
0:2 berarti baris dari indeks 0 hingga sebelum indeks 2 (baris 0 dan baris 1).
2 di sini adalah indeks kolom. Ini berarti kita memilih elemen pada kolom dengan indeks 2.
Jadi, kita mengambil elemen pada baris 0 dan baris 1 dari kolom dengan indeks 2.
"""

# Dari kedua elemen, Slicing indeks 1 ke indeks 4 (tidak termasuk), ini akan mengembalikan array 2-D
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])