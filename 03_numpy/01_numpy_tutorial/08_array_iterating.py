"""
Array Iterasi => menelusuri elemen satu per satu.
  1. Saat kita menangani array multidimensi di numpy, kita dapat melakukannya menggunakan for loop dasar python.
  2. Jika kita melakukan iterasi pada array 1-D, ia akan melewati setiap elemen satu per satu.

Iterasi Array 2-D
  Dalam larik 2D, ia akan melewati semua baris.

Jika kita melakukan iterasi pada array n -D maka array tersebut akan melewati dimensi ke-n ke-1 satu per satu.

Untuk mengembalikan nilai sebenarnya, skalar, kita harus mengulangi array di setiap dimensi.

Iterasi Array 3-D
  Dalam array 3-D, ia akan melewati semua array 2-D

Iterasi Array Menggunakan nditer()
  Fungsi tersebut nditer()merupakan fungsi bantuan yang dapat digunakan dari iterasi paling dasar hingga sangat lanjut.
  Ini memecahkan beberapa masalah dasar yang kita hadapi dalam iterasi, mari kita bahas dengan contoh.

Iterasi pada Setiap Elemen Skalar
  Dalam forloop dasar, melakukan iterasi melalui setiap skalar array kita perlu menggunakan n for loop yang mungkin sulit untuk ditulis untuk array dengan dimensi yang sangat tinggi.

Iterasi Array Dengan Tipe Data Berbeda
  1. Kita dapat menggunakan op_dtypes argumen dan meneruskan tipe data yang diharapkan untuk mengubah tipe data elemen saat melakukan iterasi.
  2. NumPy tidak mengubah tipe data elemen di tempat (di mana elemen berada dalam array) sehingga memerlukan ruang lain untuk melakukan tindakan ini, ruang tambahan tersebut disebut buffer, dan untuk mengaktifkannya nditer() kita meneruskannya flags=['buffered'].

Iterasi Dengan Ukuran Langkah Berbeda
  Kita bisa menggunakan filtering dan dilanjutkan dengan iterasi.

Iterasi yang Dihitung Menggunakan ndenumerate()
  1. Pencacahan artinya menyebutkan nomor urut sesuatu satu per satu.
  2. Terkadang kita memerlukan indeks elemen yang sesuai saat melakukan iterasi, ndenumerate() metode ini dapat digunakan untuk kasus penggunaan tersebut.
"""
## Array Iterasi
# Ulangi elemen array 1-D berikut
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)

## Iterasi Array 2-D
# Ulangi elemen array 2-D berikut
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

# Ulangi setiap elemen skalar array 2-D
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

## Iterasi Array 3-D
# Ulangi elemen array 3-D berikut
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

# Untuk mengembalikan nilai sebenarnya, skalar, kita harus mengulangi array di setiap dimensi.
# Iterasi ke skalar
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)

## Iterasi Array Menggunakan nditer()
# Iterasi melalui array 3-D berikut
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

## Iterasi Array Dengan Tipe Data Berbeda
# Iterasi melalui array sebagai string
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

## Iterasi Dengan Ukuran Langkah Berbeda
# Ulangi setiap elemen skalar array 2D dengan melewatkan 1 elemen
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

## Iterasi yang Dihitung Menggunakan ndenumerate()
# Hitung elemen array 1D berikut
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

# Hitung elemen array 2D berikut
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)