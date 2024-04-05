"""
1. Untuk membuat ndarray, kita bisa meneruskan list, tuple, atau objek mirip array apa pun ke dalam array() metode, dan itu akan diubah menjadi ndarray

Dimensi dalam array adalah satu tingkat kedalaman array (array bersarang).
1. array bersarang: adalah array yang memiliki array sebagai elemennya.
2. Array 0-D, atau Skalar, adalah elemen dalam array. Setiap nilai dalam array adalah array 0-D
3. Array yang memiliki array 0-D sebagai elemennya disebut array unidimensi atau array 1-D.
4. Array yang memiliki array 1-D sebagai elemennya disebut array 2-D
    - Ini sering digunakan untuk merepresentasikan matriks atau tensor orde 2.
    - NumPy memiliki seluruh sub modul yang didedikasikan untuk operasi matriks yang disebut numpy.mat
5. Array yang memiliki array 2D (matriks) sebagai elemennya disebut array 3D
    Ini sering digunakan untuk mewakili tensor orde ke-3.
6. NumPy Arrays menyediakan ndim atribut yang mengembalikan bilangan bulat yang memberi tahu kita berapa banyak dimensi yang dimiliki array.
7. Saat array dibuat, Kita dapat menentukan jumlah dimensi dengan menggunakan ndmin argumen.


"""

# 1. contoh Tuple membuat array
import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)

# 2. Buat array 0-D dengan nilai 42
arr = np.array(42)

print(arr)

# 3. Buat array 1-D yang berisi nilai 1,2,3,4,5
arr = np.array([1, 2, 3, 4, 5])

print(arr)

# 4. Buat array 2D yang berisi dua array dengan nilai 1,2,3 dan 4,5,6
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

# 5. Buat array 3-D dengan dua array 2-D, keduanya berisi dua array dengan nilai 1,2,3 dan 4,5,6
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

# 6. Periksa berapa banyak dimensi yang dimiliki array
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# 7. Buat array dengan 5 dimensi dan verifikasi bahwa array tersebut memiliki 5 dimensi
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

"""
Pada array ini dimensi paling dalam (dim ke-5) mempunyai 4 elemen
redup ke-4 mempunyai 1 elemen yaitu vektor
redup ke-3 mempunyai 1 elemen yaitu matriks dengan vektor
redup ke-2 mempunyai 1 elemen yaitu array 3D dan Dim pertama memiliki 1 elemen yaitu array 4D.
"""