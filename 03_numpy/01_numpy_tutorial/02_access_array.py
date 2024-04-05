"""
Akses Elemen Array
    1. Pengindeksan array sama dengan mengakses elemen array.
    2. Kita dapat mengakses elemen array dengan mengacu pada nomor indeksnya.
    3. Indeks dalam array NumPy dimulai dengan 0, artinya elemen pertama memiliki indeks 0, dan elemen kedua memiliki indeks 1, dll.

Akses Array 2-D
    1. Untuk mengakses elemen dari array 2D kita dapat menggunakan bilangan bulat yang dipisahkan koma yang mewakili dimensi dan indeks elemen.
    2. Bayangkan array 2D seperti tabel dengan baris dan kolom, yang dimensinya mewakili baris dan indeks mewakili kolom.

Akses Array 3-D
    Untuk mengakses elemen dari array 3-D kita dapat menggunakan bilangan bulat yang dipisahkan koma yang mewakili dimensi dan indeks elemen.

Pengindeksan Negatif
    Gunakan pengindeksan negatif untuk mengakses array dari akhir.
"""
## 1. Akses Elemen Array
# Dapatkan elemen pertama dari array berikut
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

# Dapatkan elemen kedua dari array berikut.
arr = np.array([1, 2, 3, 4])

print(arr[1])

# Dapatkan elemen ketiga dan keempat dari array berikut dan tambahkan.
arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])


## 2. Akses Array 2-D
# Akses elemen pada baris pertama, kolom kedua
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

# Akses elemen pada baris ke-2, kolom ke-5
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])


## 3. Akses Array 3-D
# Akses elemen ketiga dari array kedua dari array pertama
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2]) # hasil 6

"""
Penjelasan contoh 3. Akses Array 3-D
    Angka pertama mewakili dimensi pertama, yang berisi dua larik:
    [[1, 2, 3], [4, 5, 6]]
    dan:
    [[7, 8, 9], [10, 11, 12]]
    Sejak kita pilih 0, yang tersisa adalah array pertama:
    [[1, 2, 3], [4, 5, 6]]
    
    Angka kedua mewakili dimensi kedua, yang juga berisi dua larik:
    [1, 2, 3]
    dan:
    [4, 5, 6]
    Karena kita memilih 1, yang tersisa adalah larik kedua:
    [4, 5, 6]
    
    Karena kita memilih 2, kita mendapatkan nilai ketiga:
    6
"""

## Cetak elemen terakhir dari 2nd dim
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])