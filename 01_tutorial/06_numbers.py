'''
1. Ada tiga tipe numerik dalam Python:
   - int
   - float
   - complex
2. Int
    bilangan bulat => positif atau negatif, tanpa desimal, dan panjangnya tidak terbatas
3. Float
    bilangan desimal => positif atau negatif yang mengandung satu atau lebih desimal.
    bilangan ilmiah dengan huruf "e" untuk menunjukkan pangkat 10
4. Complex number
    ditulis dengan huruf "j" sebagai bagian imajinernya
5. Jenis Konversi
    Dapat mengonversi dari satu tipe ke tipe lainnya dengan metode int(), float(), dan complex()
6. Random Number
    Python memiliki modul bawaan bernama randomyang dapat digunakan untuk membuat angka acak
'''

## Contoh
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

# Contoh Int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Contoh Float => bilangan desimal
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Contoh Float => bilangan ilmiah
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Contoh Kompleks
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

## Contoh Konversi
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

## Contoh Random Number
import random

print(random.randrange(1, 10))