"""
Aritmatika Sederhana
1. Anda dapat menggunakan operator aritmatika + - * / secara langsung di antara array NumPy,
    tetapi bagian ini membahas perluasan yang sama di mana kita memiliki fungsi yang dapat mengambil objek seperti array misalnya list, tupel, dll.
    dan melakukan aritmatika secara kondisional.
2. Aritmatika Bersyarat: artinya kita dapat menentukan kondisi di mana operasi aritmatika harus dilakukan
3. Semua fungsi aritmatika yang dibahas mengambil where parameter yang dapat kita tentukan kondisinya.
    - Fungsi add()                  menjumlahkan konten dari dua array, dan mengembalikan hasilnya dalam array baru
    - Fungsi subtract()             mengurangi nilai dari satu array dengan nilai dari array lain, dan mengembalikan hasilnya dalam array baru.
    - Fungsi multiply()             mengalikan nilai dari satu array dengan nilai dari array lain, dan mengembalikan hasilnya dalam array baru.
    - Fungsi divide()               membagi nilai dari satu array dengan nilai dari array lain, dan mengembalikan hasilnya dalam array baru.
    - Fungsi power()                menaikkan nilai dari larik pertama ke pangkat nilai larik kedua, dan mengembalikan hasilnya dalam larik baru.
    - Fungsi mod() dan remainder()  mengembalikan sisa nilai dalam larik pertama yang sesuai dengan nilai dalam larik kedua, dan mengembalikan hasilnya dalam larik baru.
    - Fungsi divmod()               mengembalikan hasil bagi dan mod. Nilai yang dikembalikan adalah dua larik, larik pertama berisi hasil bagi dan larik kedua berisi mod.
    - fungsi absolute() dan abs()   fungsinya melakukan operasi absolut yang sama dari segi elemen, tetapi kita harus menggunakannya absolute() untuk menghindari kebingungan dengan bawaan pythonmath.abs()
"""
## Add
# Tambahkan nilai di arr1 ke nilai di arr2
import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)

# Contoh di atas akan mengembalikan [30 32 34 36 38 40] yang merupakan jumlah dari 10+20, 11+21, 12+22 dst

## Subtraction
# Kurangi nilai di arr2 dari nilai di arr1
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)

# Contoh di atas akan mengembalikan [-10 -1 8 17 26 35] yang merupakan hasil dari 10-20, 20-21, 30-22 dst.

## Multiplication
# Kalikan nilai di arr1 dengan nilai di arr2
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)

# Contoh di atas akan mengembalikan [200 420 660 920 1200 1500] yang merupakan hasil 10*20, 20*21, 30*22 dst.

## Division
# Bagilah nilai di arr1 dengan nilai di arr2
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)

# Contoh di atas akan mengembalikan [3.33333333 4.3.5.25.1.81818182] yang merupakan hasil dari 10/3, 20/5, 30/10 dst.

## power
# Naikkan nilai di arr1 ke pangkat nilai di arr2
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)

# Contoh di atas akan mengembalikan [1000 3200000 729000000 6553600000000 2500 0] yang merupakan hasil dari 10*10*10, 20*20*20*20*20, 30*30*30*30*30*30 dst.

## Remainder
# Kembalikan sisanya
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)

print(newarr)

# Contoh di atas akan menghasilkan [1 6 3 0 0 27] yang merupakan sisa ketika Anda membagi 10 dengan 3 (10%3), 20 dengan 7 (20%7), 30 dengan 9 (30%9) dan seterusnya.

# Anda mendapatkan hasil yang sama saat menggunakan remainder()fungsi
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.remainder(arr1, arr2)

print(newarr)

## Quotient and Mod
# Kembalikan hasil bagi dan mod
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr)

# Contoh di atas akan menghasilkan:
# (array([3, 2, 3, 5, 25, 1]), array([1, 6, 3, 0, 0, 27]))
# Array pertama mewakili hasil bagi, (the nilai integer ketika Anda membagi 10 dengan 3, 20 dengan 7, 30 dengan 9 dst.
# Array kedua mewakili sisa pembagian yang sama.

## Absolute Values
# Kembalikan hasil bagi dan mod
import numpy as np

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr)

# Contoh di atas akan mengembalikan [1 2 1 2 3 4].