"""
Untuk mencari hasil kali elemen-elemen dalam array, gunakan fungsi prod().

Product Over an Axis
    Jika Kita menentukan axis=1, NumPy akan mengalikan angka di setiap larik.

Cummulative Product
    - Product kumulatif berarti mengalikan sebagian elemen dalam array.
    - Misalnya, produk parsial dari [1, 2, 3, 4] adalah [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24].
    - Lakukan perkalian sebagian dengan cumprod()fungsi tersebut.
"""
## Product
# Temukan produk dari elemen array ini
import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x)
"""
Pengembalian: 24 karena 1*2*3*4 = 24
"""

# Temukan produk elemen dari dua array
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print(x)
"""
Pengembalian: 40320 karena 1*2*3*4*5*6*7*8 = 40320
"""


## Product Over an Axis
# Lakukan penjumlahan dalam array berikut pada sumbu pertama
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)
"""
1*2*3*4 = 24
5*6*7*8 = 1680
"""

## Cummulative Product
# Lakukan perkalian kumulatif dari semua elemen untuk array berikut
import numpy as np

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)
"""
Pengembalian: [  5  30 210 1680] karena 5, 5*6, 5*6*7, 5*6*7*8
"""