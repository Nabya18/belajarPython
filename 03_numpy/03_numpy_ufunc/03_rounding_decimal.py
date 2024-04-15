"""
Pembulatan Desimal
Ada lima cara utama untuk membulatkan desimal di NumPy:
    - truncation: Hapus desimal, dan kembalikan angka float yang paling dekat dengan nol. Gunakan fungsi trunc().
    - fix: seperti truncation. Fungsi fix() Hapus desimal, dan kembalikan angka float yang paling dekat dengan nol.
    - rounding: Fungsi around() bertambah sebelum digit atau desimal sebesar 1 jika >=5, jika tidak, itu tidak berubah.
    - floor: Fungsi floor() membulatkan desimal ke bilangan bulat terdekat yang lebih rendah.
    - ceil: Fungsi ceil() membulatkan desimal ke bilangan bulat atas terdekat.
"""
## Truncation
# Potong elemen array berikut
import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)

# Contoh yang sama, menggunakan fix()
arr = np.fix([-3.1666, 3.6667])

print(arr)

## Rounding
# Bulatkan 3,1666 menjadi 2 desimal
arr = np.around(3.1666, 2)

print(arr)

## Floor
arr = np.floor([-3.1666, 3.6667])

print(arr)

## Ceil
arr = np.ceil([-3.1666, 3.6667])

print(arr)