"""
Differences
    1. Perbedaan diskrit berarti mengurangkan dua elemen yang berurutan.
    2. Misalnya untuk [1, 2, 3, 4], selisih diskritnya adalah [2-1, 3-2, 4-3] = [1, 1, 1]
    3. Untuk mencari selisih diskrit, gunakan diff() fungsi.

1. Kita dapat melakukan operasi ini berulang kali dengan memberikan parameter n.
2. Misalnya untuk [1, 2, 3, 4], selisih diskrit dengan n = 2 adalah [2-1, 3-2, 4-3] = [1, 1, 1] ,
    maka, karena n=2, kita akan melakukannya sekali lagi, dengan hasil baru: [1-1, 1-1] = [0, 0]
"""
# Hitung perbedaan diskrit dari array berikut
import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)
"""
Pengembalian: [5 10 -20] karena 15-10=5, 25-15=10, dan 5-25=-20
"""

# Hitung perbedaan diskrit dari array berikut dua kali
import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr, n=3)

print(newarr)
"""
Pengembalian: [-35] karena: 
[15-10=5, 25-15=10, 5-25=-20]
[10-5=5, -20-10=-30]
[-30-5=-35]
"""