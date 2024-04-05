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
"""
Iterasi langsung melalui elemen-elemen array 1-D dilakukan dengan loop for. Setiap elemen diprint satu per satu.
"""


## Iterasi Array 2-D
# Ulangi elemen array 2-D berikut
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)
"""
Dalam kasus ini, setiap iterasi menghasilkan baris array 2-D, karena array 2-D terdiri dari baris-baris yang berisi elemen-elemen tersebut.
"""


# Ulangi setiap elemen skalar array 2-D
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
"""
Iterasi dilakukan secara bertingkat, dengan loop luar mengakses setiap baris, dan loop dalam mengakses setiap elemen dalam baris tersebut.
"""


## Iterasi Array 3-D
# Ulangi elemen array 3-D berikut
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)
"""
Dalam kasus ini, setiap iterasi menghasilkan matriks 2-D (sub-array) dari array 3-D. Sehingga, kita melihat matriks-matriks tersebut sebagai output iterasi.
"""


# Untuk mengembalikan nilai sebenarnya, skalar, kita harus mengulangi array di setiap dimensi.
# Iterasi ke skalar
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
"""
Iterasi dilakukan secara bertingkat melalui setiap dimensi array, sehingga kita bisa mengakses setiap elemen skalar dalam array 3-D.
"""


## Iterasi Array Menggunakan nditer()
# Iterasi melalui array 3-D berikut
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
"""
nditer() adalah metode yang lebih fleksibel untuk melakukan iterasi pada array NumPy, yang secara otomatis menyesuaikan langkah iterasi sesuai dengan dimensi array.
"""


## Iterasi Array Dengan Tipe Data Berbeda
# Iterasi melalui array sebagai string
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
"""
Dalam contoh ini, kita menggunakan nditer() untuk mengiterasi melalui array NumPy
dan dengan parameter op_dtypes=['S'], kita memaksa setiap elemen untuk diinterpretasikan sebagai string ('S')
"""


## Iterasi Dengan Ukuran Langkah Berbeda
# Ulangi setiap elemen skalar array 2D dengan melewatkan 1 elemen
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)
"""
Dalam contoh ini, kita menggunakan nditer() untuk mengiterasi melalui array 2-D,
tetapi hanya mempertimbangkan elemen-elemen yang dipilih dengan langkah yang berbeda (::2).
"""


## Iterasi yang Dihitung Menggunakan ndenumerate()
# Hitung elemen array 1D berikut
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

# Hitung elemen array 2D berikut
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
"""
ndenumerate() adalah fungsi yang memberikan iterator bersama dengan indeksnya
sehingga kita dapat mengetahui posisi relatif setiap elemen dalam array saat melakukan iterasi.
"""