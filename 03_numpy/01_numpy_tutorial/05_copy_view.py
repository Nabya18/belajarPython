"""
Perbedaan Antara Copy dan View
    1. Perbedaan utama antara Copy dan View array adalah Copynya adalah array baru, dan View tersebut hanyalah View dari array asli.
    2. Copy memiliki data dan perubahan apa pun yang dilakukan pada Copy tidak akan memengaruhi larik asli, dan perubahan apa pun yang dilakukan pada larik asli tidak akan memengaruhi Copy.
    3. View tidak memiliki data dan setiap perubahan yang dilakukan pada View akan memengaruhi array asli, dan setiap perubahan yang dilakukan pada array asli akan memengaruhi View.

Copynya TIDAK BOLEH terpengaruh oleh perubahan yang dilakukan pada array asli.

View HARUS dipengaruhi oleh perubahan yang dilakukan pada array asli.

Array asli HARUS terpengaruh oleh perubahan yang dilakukan pada View.

Periksa apakah Array Memiliki Datanya
    1. Setiap array NumPy memiliki atribut base yang dikembalikan Nonejika array tersebut memiliki data.
    2. Jika tidak, base  atribut akan mengacu pada objek aslinya.
"""

# Buat Copy, ubah array asli, dan tampilkan kedua array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# Buat View, ubah array asli, dan tampilkan kedua array
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# Buat View, ubah View, dan tampilkan kedua array
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

# Cetak nilai atribut dasar untuk memeriksa apakah suatu array memiliki datanya atau tidak
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

"""
Copynya kembali None.
View mengembalikan array asli.
"""