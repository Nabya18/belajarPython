"""
NumPy LCM Lowest Common Multiple / KPK (Kelipatan Persekutuan Terkecil)
    LCM adalah Kelipatan Persekutuan Terendah adalah bilangan terkecil yang merupakan kelipatan persekutuan dua bilangan.

1. Untuk mencari Kelipatan Persekutuan Terendah dari semua nilai dalam sebuah array, Kita dapat menggunakan reduce() metode ini.
2. Metode ini reduce() akan menggunakan ufunc, dalam hal ini fungsinya lcm(), pada setiap elemen, dan mengurangi array sebanyak satu dimensi.
"""
# Tentukan KPK dari dua bilangan berikut
import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)
"""
Pengembalian: 12 karena itu adalah kelipatan persekutuan terkecil dari kedua bilangan (4*3=12 dan 6*2=12).
"""

# Temukan KPK dari nilai array berikut
import numpy as np

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)
"""
Pengembalian: 18 karena itu adalah kelipatan persekutuan terkecil dari ketiga bilangan (3*6=18, 6*3=18 dan 9*2=18).
"""

# Temukan KPK dari semua nilai array yang arraynya berisi semua bilangan bulat dari 1 hingga 10
import numpy as np

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)
"""
Hasilnya adalah 2520 karena kode tersebut mencari Kelipatan Persekutuan Terkecil (KPK) dari semua bilangan bulat dari 1 hingga 10.  
Berikut adalah penjelasan langkah demi langkah:  
    1. np.arange(1, 11) menghasilkan array numpy yang berisi bilangan bulat dari 1 hingga 10.
    2. np.lcm.reduce(arr) kemudian menghitung KPK dari semua elemen dalam array tersebut.

KPK dari dua bilangan adalah bilangan terkecil yang dapat dibagi habis oleh kedua bilangan tersebut. 
Dalam hal ini, kita mencari KPK dari lebih dari dua bilangan, yaitu dari semua bilangan bulat dari 1 hingga 10.  
Jika kita menghitung secara manual, kita akan mendapatkan:  
    KPK(1, 2) = 2
    KPK(2, 3) = 6
    KPK(6, 4) = 12
    KPK(12, 5) = 60
    KPK(60, 6) = 60
    KPK(60, 7) = 420
    KPK(420, 8) = 840
    KPK(840, 9) = 2520
    KPK(2520, 10) = 2520
    
Jadi, KPK dari semua bilangan bulat dari 1 hingga 10 adalah 2520.
"""