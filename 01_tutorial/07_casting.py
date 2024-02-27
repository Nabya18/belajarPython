'''
Casting => Menentukan Jenis Variabel

Python adalah bahasa berorientasi objek, dan karena itu ia menggunakan kelas untuk mendefinisikan tipe data, termasuk tipe primitifnya.
1. Transmisi dengan python dilakukan menggunakan fungsi konstruktor:
   - int() - membuat bilangan bulat dari literal bilangan bulat, literal float (dengan menghapus semua desimal), atau literal string (asalkan string mewakili bilangan bulat)
   - float() - membuat angka float dari literal integer, literal float, atau literal string (asalkan string mewakili float atau integer)
   - str() - membuat string dari berbagai tipe data, termasuk string, literal integer, dan literal float

'''

## Casting int
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

## Casting Float
a = float(1)     # x will be 1.0
b = float(2.8)   # y will be 2.8
c = float("3")   # z will be 3.0
d = float("4.2") # w will be 4.2

## Casting String
e = str("s1") # x will be 's1'
f = str(2)    # y will be '2'
g = str(3.0)  # z will be '3.0'