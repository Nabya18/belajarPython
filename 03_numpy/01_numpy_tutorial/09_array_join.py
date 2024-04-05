"""
Join dengan Array NumPy
    1. Bergabung berarti meletakkan isi dari dua atau lebih array dalam satu array.
    2. Di SQL kita menggabungkan tabel berdasarkan kunci, sedangkan di NumPy kita menggabungkan array berdasarkan sumbu.
    3. Kita meneruskan rangkaian array yang ingin kita gabungkan ke concatenate()fungsi, bersama dengan sumbunya. Jika sumbu tidak dilewati secara eksplisit, maka dianggap 0.

Menggabungkan Array Menggunakan Fungsi Stack
    1. Penumpukan sama dengan penggabungan, perbedaannya hanya penumpukan dilakukan sepanjang sumbu baru.
    2. Kita dapat menggabungkan dua larik 1-D di sepanjang sumbu kedua yang akan menghasilkan penempatan keduanya, yaitu. menumpuk.
    3. Kami meneruskan urutan array yang ingin kami gabungkan ke stack()metode bersama dengan sumbunya. Jika sumbu tidak dilewati secara eksplisit maka dianggap 0.

Menumpuk Sepanjang Baris
    NumPy menyediakan fungsi pembantu: hstack() untuk menumpuk di sepanjang baris.

Menumpuk Sepanjang Kolom
    NumPy menyediakan fungsi pembantu: vstack()  untuk menumpuk di sepanjang kolom.

Penumpukan Sepanjang Ketinggian (kedalaman)
    NumPy menyediakan fungsi pembantu: dstack() untuk menumpuk sepanjang ketinggian, yang sama dengan kedalaman.
"""
## Join dengan Array NumPy
# Bergabunglah dengan dua array
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

# Gabungkan dua array 2-D sepanjang baris (sumbu=1)
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

## Menggabungkan Array Menggunakan Fungsi Stack
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

## Menumpuk Sepanjang Kolom
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)

## Penumpukan Sepanjang Ketinggian (kedalaman) / dipasangkan sesuai urutan
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)