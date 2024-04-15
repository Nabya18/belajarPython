"""
Apa perbedaan dari summation dan addition?
    Addition dilakukan antara dua argumen sedangkan summation terjadi pada n elemen.

1. Summation Over an Axis => Jika Kita menentukan axis=1, NumPy akan menjumlahkan angka di setiap larik.
2. Cummulative Sum
    - Jumlah kumulatif berarti menambahkan sebagian elemen dalam array.
    - Misalnya, jumlah parsial dari [1, 2, 3, 4] adalah [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
    - Lakukan penjumlahan sebagian dengan cumsum()fungsi tersebut.
"""
# Addition => Tambahkan nilai di arr1 ke nilai di arr2
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)

# Summation => Jumlahkan nilai keseluruhan array
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)

# Summation Over an Axis => Lakukan penjumlahan dalam array berikut pada sumbu pertama
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)

# Cummulative Sum => Lakukan penjumlahan kumulatif dalam array berikut
import numpy as np

arr = np.array([2, 4, 10])

newarr = np.cumsum(arr)

print(newarr)
"""
seperti penjumlahan deret aritmatika, contoh
[1 2 3]
= [1 1+2 1+2+3]
= [1 3 6]
"""