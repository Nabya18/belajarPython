"""
Filtering Array
1. Mengeluarkan beberapa elemen dari array yang sudah ada dan membuat array baru dari elemen tersebut disebut pemfilteran .
2. Di NumPy, Kita memfilter array menggunakan daftar indeks boolean .

List indeks boolean adalah list boolean yang sesuai dengan indeks dalam array.
    1. Jika nilai pada indeks adalah Trueelemen tersebut terdapat dalam array yang difilter
    2. jika nilai pada indeks tersebut adalah False elemen tersebut dikecualikan dari array yang difilter.

Membuat Array Filter => berdasarkan kondisi.

Membuat Filter Langsung Dari Array
    Kita bisa langsung mengganti array dan bukan variabel iterable dalam kondisi kita dan array akan berfungsi seperti yang kita harapkan.
"""
# Buat array dari elemen pada indeks 0 dan 2
import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)
"""
Contoh di atas akan kembali [41, 43]
Karena array baru hanya berisi nilai di mana array filter memiliki nilai True, dalam hal ini indeks 0 dan 2.
"""

## Buat array filter yang hanya akan mengembalikan nilai lebih tinggi dari 42
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

## Buat array filter yang hanya akan mengembalikan elemen genap dari array asli
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

## Membuat Filter Langsung Dari Array
# Buat array filter yang hanya akan mengembalikan nilai lebih tinggi dari 42
arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Buat array filter yang hanya akan mengembalikan elemen genap dari array asli
arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)