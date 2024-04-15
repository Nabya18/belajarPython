"""
Operasi Set NumPy

Apa itu Set
    1. Himpunan dalam matematika adalah kumpulan unsur-unsur unik.
    2. Himpunan digunakan untuk operasi yang sering melibatkan operasi persimpangan, penyatuan, dan perbedaan.

Buat Set di NumPy
    Kita dapat menggunakan metode NumPy unique() untuk menemukan elemen unik dari array mana pun.
    Misalnya membuat larik himpunan, tetapi ingat bahwa larik himpunan hanya boleh berupa larik 1-D.

Menemukan Persatuan
    Persatuan berarti menggabungkan dua himpunan.
    Untuk menemukan persatuan dua himpunan, gunakan NumPy union1d() metode.

Menemukan Persimpangan
    Persimpangan berarti hanya menyimpan elemen yang ada di kedua himpunan.
    Untuk menemukan persimpangan dua himpunan, gunakan NumPy intersect1d()

Menemukan Perbedaan
    Perbedaan berarti menghapus elemen yang ada di kedua himpunan.
    Untuk menemukan perbedaan dua himpunan, gunakan NumPy setdiff1d() metode.

Menemukan Perbedaan Simetris
    Perbedaan simetris berarti menghapus elemen yang ada di kedua himpunan.
    Untuk menemukan perbedaan simetris dua himpunan, gunakan NumPy setxor1d() metode.

Catatan: metode ini intersect1d()mengambil argumen opsional assume_unique, yang jika disetel ke True dapat mempercepat komputasi. Itu harus selalu disetel ke True ketika berhadapan dengan set.
"""
# Buat Set di NumPy => Ubah array berikut dengan elemen berulang menjadi satu set
import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x)
"""
Hanya elemen unik yang tersisa, elemen berulang dihapus.
"""

# Menemukan Persatuan => Temukan persatuan dari dua set berikut
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)
"""
Elemen yang sama hanya muncul sekali, elemen berulang dihapus.
"""

# Menemukan Persimpangan => Temukan persimpangan dari dua set berikut
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.intersect1d(arr1, arr2, assume_unique=True)

print(newarr)
"""
Hanya elemen yang ada di kedua set yang diambil.
"""

# Menemukan Perbedaan => Temukan perbedaan set1 dari set2
import numpy as np

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique=True)

print(newarr)
"""
Elemen yang ada di set1 tetapi yang sama dan berbeda di set2 tidak diambil.
"""

# Menemukan Perbedaan Simetris => Temukan perbedaan simetris dari himpunan1 dan himpunan2
import numpy as np

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr)
"""
Hanya yang berbeda di kedua set yang diambil.
"""