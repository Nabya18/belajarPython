"""
Secara default Python memiliki tipe data berikut:
    strings-    digunakan untuk mewakili data teks, teks diberikan di bawah tanda kutip. misalnya "ABCD"
    integer-    digunakan untuk mewakili bilangan bulat. misalnya -1, -2, -3
    float-      digunakan untuk mewakili bilangan real. misalnya 1.2, 42.42
    boolean-    digunakan untuk mewakili Benar atau Salah.
    complex-    digunakan untuk mewakili bilangan kompleks. misalnya 1.0 + 2.0j, 1.5 + 2.5j

NumPy memiliki beberapa tipe data tambahan, dan mengacu pada tipe data dengan satu karakter, seperti i bilangan bulat, u bilangan bulat tak bertanda, dll.

Di bawah ini adalah daftar semua tipe data di NumPy dan karakter yang digunakan untuk mewakilinya.
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
Untuk i, u, f, Sdan Ukita dapat menentukan ukurannya juga.

Objek array NumPy memiliki properti bernama dtype yang mengembalikan tipe data array

Membuat Array Dengan Tipe Data yang Ditentukan
Kita menggunakan array() fungsi ini untuk membuat array, fungsi ini dapat mengambil argumen opsional: dtype yang memungkinkan kita menentukan tipe data yang diharapkan dari elemen array

Jika suatu tipe diberikan di mana elemen tidak dapat casted maka NumPy akan memunculkan ValueError.
ValueError: Dalam Python ValueError dimunculkan ketika tipe argumen yang diteruskan ke suatu fungsi tidak terduga/salah.

Mengonversi Tipe Data pada Array yang Ada
    1. Cara terbaik untuk mengubah tipe data array yang ada adalah dengan membuat salinan array dengan astype()metode tersebut.
    2. Fungsi ini astype()membuat salinan array, dan memungkinkan Anda menentukan tipe data sebagai parameter.
    3. Tipe data dapat ditentukan menggunakan string, seperti 'f'untuk float, 'i'untuk integer, dll. atau Anda dapat menggunakan tipe data secara langsung seperti floatuntuk float dan intinteger.
"""

## Memeriksa Tipe Data Array
# Dapatkan tipe data objek array
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

# Dapatkan tipe data array yang berisi string
arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

"""
Hasil <U6 menunjukkan tipe data dari array arr. Tipe data <U6 menandakan bahwa ini adalah array unicode dengan panjang maksimum 6 karakter.
    <U  menunjukkan unicode string.
    6   menunjukkan panjang maksimum string dalam array tersebut.
"""

## Membuat Array Dengan Tipe Data yang Ditentukan
# Buat array dengan tipe data string
arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

# Buat array dengan tipe data integer 4 byte
arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

## Mengonversi Tipe Data pada Array yang Ada
# Ubah tipe data dari float menjadi integer dengan menggunakan 'i' nilai parameter
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

# Ubah tipe data dari float menjadi integer dengan menggunakan intnilai parameter
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

# Ubah tipe data dari integer menjadi boolean
arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)