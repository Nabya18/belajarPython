"""
Finding GCD (Greatest Common Denominator) / FPB (Faktor Persekutuan Terbesar)
    GCD adalah bilangan terbesar yang dapat membagi habis kedua bilangan.

1. Untuk mencari Faktor Persekutuan Terbesar dari semua nilai dalam sebuah array, Kita dapat menggunakan reduce() metode ini.
2. Metode ini reduce() akan menggunakan ufunc, dalam hal ini fungsinya gcd(), pada setiap elemen, dan mengurangi array sebanyak satu dimensi.
"""
# Tentukan FPB dari dua bilangan berikut
import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x)
"""
Pengembalian: 3 karena itu adalah angka tertinggi, kedua angka tersebut dapat dibagi (6/3=2 dan 9/3=3).
"""

# Temukan FPB dari nilai array berikut
import numpy as np

arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)
"""
Pengembalian: 4 karena itu adalah angka tertinggi yang dapat membagi semua nilai.

Hasilnya adalah 4 karena kode tersebut mencari Faktor Persekutuan Terbesar (FPB) dari semua bilangan dalam array tersebut.  
Berikut adalah penjelasan langkah demi langkah:  
    1. np.array([20, 8, 32, 36, 16]) menghasilkan array numpy yang berisi bilangan tersebut.
    2. np.gcd.reduce(arr) kemudian menghitung FPB dari semua elemen dalam array tersebut.

FPB dari dua bilangan adalah bilangan terbesar yang dapat membagi habis kedua bilangan tersebut. 
Dalam hal ini, kita mencari FPB dari lebih dari dua bilangan, yaitu dari semua bilangan dalam array tersebut.  
Jika kita menghitung secara manual, kita akan mendapatkan:  
    FPB(20, 8) = 4
    FPB(4, 32) = 4
    FPB(4, 36) = 4
    FPB(4, 16) = 4

Jadi, FPB dari semua bilangan dalam array tersebut adalah 4. Meskipun 2 dapat membagi habis semua bilangan tersebut, 
4 adalah faktor persekutuan terbesar, sehingga hasilnya adalah 4, bukan 2.
"""