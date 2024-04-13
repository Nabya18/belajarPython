"""
ufuncs adalah singkatan dari "Fungsi Universal" dan merupakan fungsi NumPy yang beroperasi pada ndarrayobjek.
    1. ufuncs digunakan untuk mengimplementasikan vektorisasi di NumPy yang jauh lebih cepat daripada mengulangi elemen.
    2. Mereka juga menyediakan penyiaran dan metode tambahan seperti pengurangan, akumulasi, dll. yang sangat membantu untuk komputasi.
    3. ufuncs juga mengambil argumen tambahan, seperti:
        - where     array boolean atau kondisi yang menentukan di mana operasi harus dilakukan.
        - dtype     mendefinisikan tipe kembalinya elemen.
        - out       array keluaran tempat nilai kembalian harus disalin.

Apa itu Vektorisasi?
    1. Mengubah pernyataan berulang menjadi operasi berbasis vektor disebut vektorisasi.
    2. Ini lebih cepat karena CPU modern dioptimalkan untuk operasi semacam itu.

Add Elemen Dua List
List 1: [1, 2, 3, 4]
List 2: [4, 5, 6, 7]
Salah satu cara untuk melakukannya adalah dengan mengulangi kedua daftar dan kemudian menjumlahkan setiap elemen.

NumPy memiliki ufunc untuk ini, yang disebut add(x, y) akan menghasilkan hasil yang sama dengan zip().
"""
# Tanpa ufunc, kita bisa menggunakan metode bawaan Python zip()
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

# Dengan ufunc, kita dapat menggunakan add() fungsi
import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)

"""
Kode ini menggunakan NumPy untuk melakukan penjumlahan elemen-elemen dari dua list, x dan y, menggunakan fungsi np.add(). 
Hasilnya adalah sebuah array NumPy yang berisi penjumlahan dari setiap pasangan elemen yang sesuai dari x dan y.

Misalnya, jika x = [1, 2, 3, 4] dan y = [4, 5, 6, 7], hasil penjumlahannya akan menghasilkan:

z=[1+4,2+5,3+6,4+7]=[5,7,9,11]

Jadi, z akan menjadi [5, 7, 9, 11].

Dalam konteks aplikasi, ini digunakan untuk melakukan penjumlahan vektor atau array dalam analisis matematis, pemrosesan data, dan berbagai aplikasi ilmiah dan teknis lainnya.
"""