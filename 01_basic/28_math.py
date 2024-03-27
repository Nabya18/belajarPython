"""
Matematika Python
    Python memiliki serangkaian fungsi matematika bawaan, termasuk modul matematika ekstensif, yang memungkinkan Kita melakukan tugas matematika pada angka.

1. Fungsi Matematika Bawaan
    a. Fungsi min() and max() dapat digunakan untuk mencari nilai terendah atau tertinggi dalam sebuah iterable
    b. Fungsi ini abs() mengembalikan nilai absolut (positif) dari angka yang ditentukan
    c. Fungsi ini mengembalikan nilai x pangkat y. pow(x, y)

2. Modul Matematika
    a. Python juga memiliki modul bawaan yang disebut math, yang memperluas daftar fungsi matematika.
    b. Untuk menggunakannya, Kita harus mengimpor math modul:
        import math
    c. Ketika Kita telah mengimpor mathmodul, Kita dapat mulai menggunakan metode dan konstanta modul.
    d. math.sqrt() => Misalnya, metode ini mengembalikan akar kuadrat suatu angka
    e. math.ceil() => membulatkan angka ke atas hingga bilangan bulat terdekat
    f. math.floor() => metode membulatkan angka ke bawah hingga bilangan bulat terdekat, dan mengembalikan hasilnya
    g. Konstanta math.pi => mengembalikan nilai PI (3.14...)
"""
## Fungsi Matematika Bawaan
# Fungsi min() and max()
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# Fungsi abs()
x = abs(-7.25)

print(x)

# Fungsi pow(x, y) => Kembalikan nilai 4 ke pangkat 3
x = pow(4, 3)

print(x)

## Modul Matematika
# math.sqrt()
import math
x = math.sqrt(64)

print(x)

# math.ceil() and math.floor()
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

# math.pi
import math

x = math.pi

print(x)