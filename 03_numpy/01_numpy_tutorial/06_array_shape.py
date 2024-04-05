"""
Array shape => jumlah elemen di setiap dimensi

Array NumPy memiliki atribut yang disebut shape yang mengembalikan tupel dengan setiap indeks memiliki jumlah elemen yang sesuai.

Apa yang diwakili oleh tupel shape
    1. Bilangan bulat pada setiap indeks menunjukkan jumlah elemen yang dimiliki dimensi terkait
    2. Pada contoh di atas pada indeks-4 kita mempunyai nilai 4, sehingga kita dapat mengatakan bahwa dimensi ke-5 (4 + 1 th) mempunyai 4 elemen.
"""

# array 2-D
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

# Buat array dengan 5 dimensi menggunakan ndmin vektor dengan nilai 1,2,3,4 dan verifikasi bahwa dimensi terakhir memiliki nilai 4
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)