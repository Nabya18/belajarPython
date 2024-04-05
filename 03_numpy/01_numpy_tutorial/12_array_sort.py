"""
Sorting Array
    1. Menyortir berarti meletakkan elemen-elemen dalam urutan yang teratur .
    2. Urutan terurut adalah urutan apa pun yang memiliki urutan sesuai dengan elemen, seperti numerik atau alfabet, menaik atau menurun.
    3. Objek NumPy ndarray memiliki fungsi yang disebut sort(), yang akan mengurutkan array tertentu.
    4. Catatan: Metode ini mengembalikan salinan array, membiarkan array asli tidak berubah.

Menyortir Array 2-D
    Jika Kita menggunakan metode sort() pada array 2D, kedua array akan diurutkan
"""
# Urutkan susunannya
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

# Urutkan array berdasarkan abjad
arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

# Urutkan array boolean
arr = np.array([True, False, True])

print(np.sort(arr))

# Urutkan array 2-D
arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))