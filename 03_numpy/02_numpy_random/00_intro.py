"""
Random number => sesuatu yang tidak dapat diprediksi secara logika.

Pseudo Random and True Random.
    1. Komputer bekerja berdasarkan program, dan program adalah serangkaian instruksi yang pasti. Artinya harus ada algoritma untuk menghasilkan bilangan acak juga.
    2. Jika ada program untuk menghasilkan bilangan acak maka bilangan tersebut dapat diprediksi, sehingga tidak benar-benar acak.
    3. Bilangan acak yang dihasilkan melalui algoritma pembangkitan disebut acak semu .
    4. Bisakah kita membuat angka yang benar-benar acak?
        - Ya. Untuk menghasilkan angka yang benar-benar acak di komputer kita, kita perlu mendapatkan data acak dari sumber luar. Sumber luar ini umumnya adalah penekanan tombol, gerakan mouse, data di jaringan, dll.
        - Kita tidak membutuhkan angka yang benar-benar acak, kecuali jika berkaitan dengan keamanan (misalnya kunci enkripsi) atau dasar penerapannya adalah keacakan (misalnya Roda Roulette Digital).

NumPy menawarkan randommodul untuk bekerja dengan angka acak.

Hasilkan Array Acak
    1. bilangan bulat      : Metode randint() mengambil size parameter di mana Kita dapat menentukan bentuk array.
    2. bilangan desimal    :

Hasilkan Nomor Acak Dari Array
    1. choice() => memungkinkan Kita menghasilkan nilai acak berdasarkan serangkaian nilai.
    2. choice() => mengambil array sebagai parameter dan mengembalikan salah satu nilainya secara acak.
    3. choice() => juga memungkinkan Kita mengembalikan serangkaian nilai.
    4. Tambahkan size parameter untuk menentukan bentuk array.


"""
## Hasilkan Nomor Acak
from numpy import random

x = random.randint(100)

print(x)

## Hasilkan Float Acak
x = random.rand()

print(x)


### Hasilkan Array Acak
## bilangan bulat
# asilkan array 1-D yang berisi 5 bilangan bulat acak dari 0 hingga 100
x=random.randint(100, size=(5))

print(x)

# Hasilkan array 2D dengan 3 baris, setiap baris berisi 5 bilangan bulat acak dari 0 hingga 100
x = random.randint(100, size=(3, 5))

print(x)

## bilangan desimal
# Hasilkan array 1-D yang berisi 5 float acak
x = random.rand(5)

print(x)

# Hasilkan array 2D dengan 3 baris, setiap baris berisi 5 angka acak
x = random.rand(3, 5)

print(x)


## Hasilkan Nomor Acak Dari Array
# Kembalikan salah satu nilai dalam array
x = random.choice([3, 5, 7, 9])

print(x)

# Hasilkan array 2D yang terdiri dari nilai dalam parameter array (3, 5, 7, dan 9)
x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)